#!/bin/sh
docker build -t fileshare .
docker run -dt -p 9234:49760  --name fileshare fileshare
