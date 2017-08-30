#!/usr/bin/env python3
f=open("BINARY","r")
n=open("BACON","r")
ll=n.readlines()
lll=[]
hh=""
zz=""
for i in ll:
    lll.append(i.strip())
l=f.readlines()
j=[]
for i in l:
    j.append(i.strip().split(" : "))
for k in j:
    h=ll[int(k[0])-1][int(k[1])-1]
    hh=hh+h
    if h.isupper():
        zz=zz+"1"
    if h.islower():
        zz=zz+"0"
n = int(zz, 2)
print("DECRYPTING...")
print("Word => ",n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(),end="\n\n")
print("Encrypted => ",hh,end="\n\n")
print("Binary => ",zz,end="\n\n")
f.close()
n.close()
