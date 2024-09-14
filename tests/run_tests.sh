#!/bin/sh
docker build -f tests/Dockerfile.test -t my-tests .
docker run --rm my-tests
