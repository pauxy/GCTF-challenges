#!/bin/sh

docker build -t cookieagent .
docker run -it --rm -p 9911:8080 --name cookieagent cookieagent
docker start cookieagent
