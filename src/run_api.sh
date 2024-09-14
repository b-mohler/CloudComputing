#!/bin/sh

docker build -f src/Dockerfile.api -t my-api .
docker run --name my-api-container -p 5000:5000 -d my-api
