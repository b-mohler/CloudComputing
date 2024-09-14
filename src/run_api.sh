#!/bin/sh
cd src
docker build -f Dockerfile.api -t my-api .
docker run --name my-api-container -p 5000:5000 -d my-api
