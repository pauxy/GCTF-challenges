#!/bin/sh
docker build -t fishshoups .
docker run --restart always --memory 256M -d -p 17562:80 --name web-fishshoups fishshoups
docker start web-fishshoups
