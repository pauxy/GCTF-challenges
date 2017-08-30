#!/usr/bin/env python3
import socket
import threading
import random
lang=["English","Alphabetrium","Gazorpazorpian","Numberconian","Martian","Unition","Blitzion","Chipzion","Morphian"]

def of():
    k=open("Translation.txt","r")
    h=k.readlines()
    l=[]
    for i in h:
        k=[]
        k=i.strip().split(" -> ")
        l.append(k)
    return l;

langs=of()
def getran():
    h=""
    m=""
    e=""
    k=random.randint(1,8)
    kj=random.randint(1,8)
    while kj==k:
        kj=random.randint(1,8)
    for i in range(random.randint(1,5)):
        j=random.randint(0,len(langs)-1)
        m=m+langs[j][k]+" "
        e=e+langs[j][kj]+" "
    h="\n"+lang[k]+" text : "+m+"\n"+lang[kj]+" Translation -> "
    return e,h
    
def start(c,a):
    try:
        c.sendall('''
                        ‎         ,o§´A§§$`´´_´-=7JR&oZss
                               ,o§$$$§$§#9A______´b$$$$§o,
                              R$$$$$$*´´``´_______,o§$´§9$$?,
                            ,$$$$$$´______________,´§Lbd=II?&§
                           J$$§#§´________________|I$$$$$#b=b§b
                         ,$§__,´`_________________´|I$$$$$$$$$$$$
                         $Ad-´|IAb,,________________9$$$$$$$$$$$$$
                        `Z_´*§|I_____-_____________&$$$$$$$$$$$$§A
                        Z____´Lvd§§#d?____________`?$$$$$$$$$$$$$$b
                        Z______i$$$$$$§#b___________;´´*`´´#§$$$$$$
                        Z___,_,$$$$$$$$$$b´,________________{$$$$$§
                        Z____II$$$$$$$$$$$$$$§b,____________´,´$$$$
                        Z_____II$$$$$$$$$$$$$$§`_____________,&$$$$
                        Z_______´#$$$$$$$$$$$$____________;II$$$$6-
                         Z________`$$$$$$$$$$+_____________J$$$$$T/
                          Z_______´$$$$$$$R´________________-§$$$*´
                           Z______II$$$$$§´___________________,$#´
                            Z,_____A$$$§II____________________Z/
                             Z,____II$$______________________Z
                              `,Z____´R?,,____,___________,,7Z
                                  -,Z______,___________,Z7
                                    Z-II,Z#Zqo,,=00´´"
                                                    
                   __                  _         ___ _                  _   
                  / /  ___  _ __   ___| |_   _  / _ \ | __ _ _ __   ___| |_ 
                 / /  / _ \| '_ \ / _ \ | | | |/ /_)/ |/ _` | '_ \ / _ \ __|
                / /__| (_) | | | |  __/ | |_| / ___/| | (_| | | | |  __/ |_ 
                \____/\___/|_| |_|\___|_|\__, \/    |_|\__,_|_| |_|\___|\__|
                                         |___/                              
~~~~~WELCOME, DEAR EMPLOYEE!~~~~~
HERE AT THE GALACTIC FEDERATION, WE AIM TO PROVIDE INTERCONNECTEDNESS AMONGST PLANETS
USING OUR INTERDIMENSIONAL, INTERPLANETARY CHAT SYSTEM, LonelyPlanet HOWEVER, WE WOULD
 REQUIRE YOU TO HELP US TRANSLATE THE MESSAGES TO BE SENT\n 
'''.encode())
        c.sendall("~~~START SHIIFT~~~\n".encode())
        big=random.randint(400,420)
        k=True
        i=0
        while (i<big and k==True)==True:
            e=""
            h=""
            e,h=getran()
            c.sendall(h.strip().encode())
            c.settimeout(3.0)
            recvs=c.recv(256)
            word=recvs.decode().strip()
            word=word+" "
            if word!=e:
                k=False
            i=i+1
        if k==True:
            xx="\nYOU HAVE SUCCESSFULLY TRANSLATED FOR THE DAY! HERES YOUR FLAG\nGCTF{wu664_1u66a_du66_du66_111}\n"
        else:
            xx="\nYOU FAILED, YOUR POSITION HAS DROPPED FROM \"SENIOR TRANSLATOR\" TO \"CLERK\"\n"
        c.sendall(xx.encode())
        c.close()
    except :
        c.sendall("\nTRANSLATION TOO SLOW! FIRED!\n".encode())
        c.close()
    

       
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('0.0.0.0',59951))
socket.listen(5)
while True:
    c,a=socket.accept()
    t=threading.Thread(target=start,args=(c,a))
    t.start()
socket.close()
