#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-16 上午9:49'




import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('localhost',9001))
s.listen()


while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        system_cmd = os.popen(data.decode()).read()  #执行系统的命令
        num = len(system_cmd)
        print('system num:',num)

        conn.send( str(num).encode('utf-8') )  #返回数据的长度

        data_re = conn.recv(1024)    #长度说明客户端已经收到,然后返回给server,则正式的进行发送所有的数据
        if data_re:
            conn.send(system_cmd.encode('utf8'))

    conn.close()



