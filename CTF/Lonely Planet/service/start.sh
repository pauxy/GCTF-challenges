#!/bin/sh

docker build -t lonelyplanet .
docker run -d -p 59949:59949 --name lonelyplanet lonelyplanet
