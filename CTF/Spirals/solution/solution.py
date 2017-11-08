#!/usr/bin/env python3
import re
a = [[0 for x in range(25)] for y in range(13)]
f=open("../distrib/spiral.txt","r")
s=f.readline().strip()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, c = 0, -1, 1
l=0
for i in range(13+13-1):
    if i%2==0:
        for j in range((25+25-i)//2):
            x += dx[i % 4]
            y += dy[i % 4]
            #print(x,y,l)
            a[x][y] = s[l]
            l=l+1
            c += 1
    else:
        for j in range((13+13-i)//2):
            x += dx[i % 4]
            y += dy[i % 4]
            #print(x,y,l)
            a[x][y] = s[l]
            l=l+1
            c += 1
        
for i in a:
    for k in i:
            k=re.sub(r"¦","█",k)
            k=re.sub(r"¯","▀",k)
            k=re.sub(r"_","▄",k)
            
            print(k,end="")
    print()
