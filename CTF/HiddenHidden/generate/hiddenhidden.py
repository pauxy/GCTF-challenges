#!usr/bin/env python3
import base64

def tobin(st):
    return ''.join(['%08d'%int(bin(ord(i))[2:]) for i in st])

def b64(st):
    return base64.b64encode(st.encode('ascii')).decode()
f=open("../distrib/hiddenflag","w")
flag="GCTF{100p1n65_5_4ev44a44rz}"
for i in range(6):
    flag=b64(flag)
    flag=tobin(flag)
    print(i)
print(flag,file=f)
f.close()
