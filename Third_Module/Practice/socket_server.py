#!/usr/bin/env python
#-*- coding:utf-8 -*-


__author__ = 'andylin'
__date__ = '17-9-23 上午10:54'

import socket

server = socket.socket()
server.bind(('localhost',6969))
server.listen()

print('我要等电话')

conn, addr = server.accept()

print(conn)
print(addr)

print('电话来了')
data = conn.recv(1024)
print('recv: ',data)
conn.send(data.upper())

server.close()