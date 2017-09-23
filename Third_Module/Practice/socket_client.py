#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-23 上午10:54'


import socket



client = socket.socket()

client.connect(('localhost',6969))


client.send(b'Hello wrold!!')
data = client.recv(1024)
print('recv: ', data)

client.close()