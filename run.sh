#!/bin/bash
echo "Building docker image..."
docker build --tag url_test .
echo "Starting container..."
docker run --name url_test -p 5000:5000 url_test
