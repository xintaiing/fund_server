#!/bin/bash
docker-compose stop
yes | docker-compose rm
docker rmi fund_server_web:latest
docker-compose up -d
