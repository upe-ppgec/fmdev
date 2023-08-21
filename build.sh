#!/bin/bash

docker rmi fmdev
docker build -t fmdev:latest .

docker rm -f fmdev
docker run --rm --restart=no --network bridge \
    --name fmdev -p 5000:5000 \
    -e --verbose \
    -d fmdev
