#!/bin/sh
docker build -t haxor .
docker run --restart always --memory 64M -d -p 17651:80 --name foren-haxor haxor
docker start foren-haxor
