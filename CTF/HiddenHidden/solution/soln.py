#!/usr/bin/env python3
import base64
import re
import binascii
def decode_binary_string(s):
    n=int(s.encode(),2)
    return binascii.unhexlify('%x' % n)
def b64(s):
    return base64.b64decode(s).decode()

f=open("../distrib/hiddenflag","r")
k=f.readline()
ll=0
while True:
    if re.search(r"^GCTF{",k):
        print (k)
        break
    k=decode_binary_string(k)
    k=b64(k)
    ll=ll+1
    print(ll)
f.close()
