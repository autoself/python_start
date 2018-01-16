#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-14 下午2:03'


import socket

HOST = 'localhost'
POST = 10000

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c.connect((HOST, POST))

while True:
    name = bytes(input('>>>>'),encoding='utf8')
    if not name:
        continue
    c.sendall(name)
    data = c.recv(1024)
    print(data)

