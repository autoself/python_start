#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-11-20 下午9:57'



import socket
import os

fserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
fserver.bind(('localhost',9008))
fserver.listen()

while True:
    fconn,faddr = fserver.accept()
    print('new connet',faddr)
    while True:
        print('Please et input...')
        data = fconn.recv(1024)
        if not data:
            print('clent exit!')
            break
        cmd, filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            fs = open(filename,'rb')
            fsize = os.stat(filename).st_size
            fconn.send( str(fsize).encode('utf-8'))
            f_ack = fconn.recv(1024) # wait ack
            for line in fs:
                fconn.send(line)
            fs.close()
    fconn.close()



