#!/usr/bin/env bash

# Spin up new container for postgresql
docker rm -f posgresql-14-camunda
docker run -d \
  --name posgresql-14-camunda \
  -e "POSTGRES_PASSWORD=SuperWeakPassword123!" \
  -p 5432:5432 \
  postgres:10.13-alpine

# Wait for postgresql docker server to finish starting up
until nc -z $(docker inspect --format='{{.NetworkSettings.IPAddress}}' posgresql-14-camunda) 5432
do
    echo "waiting for postgres container to finish starting up"
    sleep 0.5
done

# Create database Camunda in postgresql
docker exec posgresql-14-camunda /usr/local/bin/createdb -U postgres "Camunda"

# Start up new camunda container connecting to database
docker rm -f camunda-postgresql
docker run -d \
  --name camunda-postgresql \
  -e "DB_DRIVER=org.postgresql.Driver" \
  -e "DB_URL=jdbc:postgresql://172.17.0.1:5432/Camunda" \
  -e "DB_USERNAME=postgres" \
  -e "DB_PASSWORD=SuperWeakPassword123!" \
  -e "TZ=Africa/Johannesburg!" \
  -p 8080:8080 \
  camunda/camunda-bpm-platform:tomcat-7.15.0

