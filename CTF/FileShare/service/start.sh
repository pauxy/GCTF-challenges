#!/bin/sh
docker pull ubuntu:14.04
docker run -i -t ubuntu /bin/bash --name fileshare fileshare
