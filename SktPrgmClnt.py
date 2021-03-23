#! /usr/bin/python3
#interpreter in the first line above

#Programmer: Amin Hasanzadeh
#Date: September 8 2018
#Purpose: Learning socket programming on client side

import socket

host = '192.168.0.31'
port = 50000
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
myMessage = 'Hello world'
s.send(myMessage.encode())
data = s.recv(size)
s.close()
print('Received from server: %s' % data)

