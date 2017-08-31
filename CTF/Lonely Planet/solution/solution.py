#/usr/bin/env python3
import socket
import re
def of():
    k=open("Translation.txt","r")
    h=k.readlines()
    l=[]
    for i in h:
        k=[]
        k=i.strip().split(" -> ")
        l.append(k)
    return l;
file=of()
lang={"English":0,"Alphabetrium":1,"Gazorpazorpian":2,"Numberconian":3,"Martian":4,"Unition":5,"Blitzion":6,"Chipzion":7,"Morphian":8}
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(("127.0.0.1",59949))
print(socket.recv(2168).decode())

k=socket.recv(248).decode()
try:
    while k!="":
        print (k,end="")# for out put purposes
        if(re.search(r"{",k)):
            break
        
        k=k.split("\n")
        sp=k[1].split(" ")[0]
        h=k[0].split(" text : ")
        k[1]=h[1].split(" ")
        k[1]=[x for x in k[1] if x]
        p=lang[h[0]]
        specified=lang[sp]
        zz="" 
        for z in k[1]:
            for i in range(0,len(file)):
                if z==file[i][p]:
                    zz=zz+file[i][specified]+" "
        zz=re.sub(" $","",zz)
        print (zz,end="\n\n")#for out put purposes
        socket.sendall(zz.encode())
        k=socket.recv(248).decode()
except :
    if k !=['']:
        print(k)
socket.close()
    
