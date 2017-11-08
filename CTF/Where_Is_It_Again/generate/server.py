#/usr/bin/env python3
import socket
import base64
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('0.0.0.0',42000))
print(socket)
socket.listen(5)
while True:
    c,a=socket.accept()
    c.sendall("Hey guy, im gon send soon hahah\n".encode())
    c.recv(256)
    c.sendall("here you go lol\n".encode())
    c.recv(256)
    with open("newflag.JPG", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        c.sendall(encoded_string)
socket.close()   

