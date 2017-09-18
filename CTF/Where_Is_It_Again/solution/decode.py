#/usr/bin/env python3
import base64
k=open("../new.jpg","wb")
with open("hello.txt", "r") as image_file:
    encoded_string = base64.b64decode(image_file.read())
    k.write(encoded_string)
