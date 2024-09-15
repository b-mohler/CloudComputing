#!/bin/sh

docker build -f Dockerfile2.test -t my-tests2 .
docker run --rm my-tests2
