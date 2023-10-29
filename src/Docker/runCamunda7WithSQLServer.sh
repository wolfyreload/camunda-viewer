#!/usr/bin/env bash

spin_up_sql_server() {
  # Spin up new container for postgresql
  docker rm -f sqlserver-9-camunda
  docker run -d \
    --name sqlserver-9-camunda \
    -e "ACCEPT_EULA=Y" \
    -e "MSSQL_SA_PASSWORD=SuperWeakPassword123!" \
    -p 1433:1433 \
    mcr.microsoft.com/mssql/server:2019-CU18-ubuntu-20.04
}

create_database() {
  # Wait for postgresql docker server to finish starting up
  until nc -z $(docker inspect --format='{{.NetworkSettings.IPAddress}}' sqlserver-9-camunda) 1433
  do
      echo "waiting for sql server container to finish starting up"
      sleep 0.5
  done

  docker exec sqlserver-9-camunda /opt/mssql-tools/bin/sqlcmd -q "CREATE DATABASE Camunda" -U sa -P SuperWeakPassword123!
}

download_sql_jdbc_driver() {
  jdbc_driver_path="https://go.microsoft.com/fwlink/?linkid=2222954"
  tar_save_name="sql-jdbc-driver.tar.gz"
  jar_name="mssql-jdbc-12.2.0.jre11.jar"

  if [ -e "${jar_name}" ]; then
    echo "File exists. Skipping download."
  else
    echo "Downloading driver"
    wget -O ${tar_save_name} "${jdbc_driver_path}"

    echo "extract jar"
    tar -zxvf ${tar_save_name} "sqljdbc_12.2/enu/${jar_name}"
    mv sqljdbc_12.2/enu/${jar_name} ./
    rm -r sqljdbc_12.2
    rm ${tar_save_name}
  fi
}

build_and_run_docker_image() {
  docker rm -f camunda-sql-server
  docker run -d \
    --name camunda-sql-server \
    -e "DB_DRIVER=com.microsoft.sqlserver.jdbc.SQLServerDriver" \
    -e "DB_URL=jdbc:sqlserver://172.17.0.1;DatabaseName=Camunda;trustServerCertificate=true;user=sa;password=SuperWeakPassword123!" \
    -e "DB_USERNAME=sa" \
    -e "DB_PASSWORD=SuperWeakPassword123!" \
    -e "TZ=Africa/Johannesburg!" \
    --mount type=bind,source="$(pwd)"/mssql-jdbc-12.2.0.jre11.jar,target=/camunda/lib/mssql-jdbc-12.2.0.jre11.jar \
    -p 8080:8080 \
    camunda/camunda-bpm-platform:tomcat-7.15.0
}

spin_up_sql_server
create_database
download_sql_jdbc_driver
build_and_run_docker_image

