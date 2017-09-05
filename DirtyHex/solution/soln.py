#!/usr/bin/env python3
import re
f=open("../distrib/flag.txt","r")
k=f.readline()
txt=re.sub(r"[^0-9a-f]","",k)
print(bytes.fromhex(txt).decode('utf-8'))
