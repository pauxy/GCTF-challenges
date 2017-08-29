#!/usr/bin/env python3
import random
import sys
f=open("BACON","r")
o=open("BINARY","w")
z=f.readlines()
k=[]
oo=""
st=sys.argv[1]
ss=''.join(['%08d'%int(bin(ord(i))[2:]) for i in st])
print("ENCRYPTING...")
print("Word => ",st,end="\n\n")

print("Encrypted => ",end="")
for i in z:
    k.append(i.strip())
for i in ss:
	if i=="1":
		j=""
		while not j.isupper():
			n=random.randint(0,13)
			b=random.randint(0,len(k[n])-1)
			j=k[n][b]
		print(j,end="")
		oo=oo+j
		print(n+1,":",b+1,file=o)
	if i=="0":
		j=""
		while not j.islower():
			n=random.randint(0,13)
			b=random.randint(0,len(k[n])-1)
			j=k[n][b]
		print(j,end="")
		oo=oo+j
		print(n+1,":",b+1,file=o)
print(end="\n\n")
print("Binary => ",ss,end="\n\n")
f.close()
o.close()
