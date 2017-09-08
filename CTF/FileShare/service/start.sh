#!/bin/sh
docker build -t fileshare .
docker run -dt -p 49760:49760  --name fileshare fileshare
