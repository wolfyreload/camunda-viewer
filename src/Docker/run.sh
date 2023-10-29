#!/bin/bash

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
  docker build . --file camunda.dockerfile --tag camunda-sql-server --no-cache
  docker rm -f camunda-sql-server
  docker run -d --name camunda-sql-server -p 8080:8080 camunda-sql-server
}

download_sql_jdbc_driver
build_and_run_docker_image

