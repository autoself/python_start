#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-14 上午10:52'



import socket
import select
import queue
import time


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9000))
server.listen()
server.setblocking(False)

client_input = [server,]
client_output = []

while True:
    readable , writeable, exceptional = select.select(client_input,client_output,client_input)
    print(readable,writeable,exceptional)
    for r in readable:
        if r is server:
            conn , addr = server.accept()
            print('conn: %',conn)
            client_input.append(conn)
        else:
            data = r.recv(1024)
            print(data)
            r.send(data)
