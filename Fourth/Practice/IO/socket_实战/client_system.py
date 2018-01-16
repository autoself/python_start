#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-16 上午9:56'



import socket


c = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
c.connect(('localhost',9001))

while True:
    data = bytes(input('>>>'),encoding='utf8')
    if not data: continue

    c.sendall(data)      #发送命令
    rnum = c.recv(1024)  #返回数据的大小

    if rnum:
        c.send(rnum)    #确认收到数据

    rescv_data = b''
    rescv_size = 0
    while rescv_size < int(rnum.decode()):
        rdata = c.recv(1024)
        rescv_size += len(rdata)
        rescv_data += rdata

    else:
        print(rescv_data.decode('utf8'))

