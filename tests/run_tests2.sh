#!/bin/sh

docker build -f Dockerfile.test -t my-tests .
docker run --rm my-tests
