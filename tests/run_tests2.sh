#!/bin/sh

docker build -f Dockerfile2.test -t my-tests .
docker run --rm my-tests
