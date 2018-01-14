#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-14 下午2:03'


import socket

HOST = '127.0.0.1'
POST = 9000

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((HOST, POST))

while True:
    name = bytes(input('>>>>'),encoding='utf8')
    c.sendall(name)
    data = c.recv(1024)
    print(data)
