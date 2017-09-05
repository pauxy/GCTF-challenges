#!/usr/bin/env python3
import random
def randomword(length):
   return ''.join(random.choice("qwsxzrgvtyhujnmkiolp") for i in range(length))
k="474354467b6d333535795f68337834643363316d616c5f31355f6234647d"
# hex for flag "GCTF{m355y_h3x4d3c1mal_15_b4d}"
f=open("../distrib/flag.txt","w")
j=""
for i in k:
	j=j+randomword(random.randint(0,10))+i
print(j,file=f)
f.close()
