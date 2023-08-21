#!/bin/bash

docker rm -f fmdev-frontend
docker rmi fmdev-frontend

docker build -t fmdev-frontend:latest .

docker run --rm --restart=no --network bridge \
    --name fmdev-frontend -p 80:80 \
    -e --verbose \
    -d fmdev-frontend
