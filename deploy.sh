#!/bin/bash
docker-compose -f docker-compose-prod.yml down
export MY_TAG=$1
docker-compose -f docker-compose-prod.yml up --build -d