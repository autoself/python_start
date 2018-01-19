#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-16 下午2:45'

import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 9002))
s.listen()

while True:

    conn, addr = s.accept()

    while True:
        cmd = conn.recv(1024).decode('utf8')
        if not cmd:continue
        files = os.path.join('/root',cmd.split(' ')[1])
        if not os.path.isfile(files):
            print('nofile')
            conn.send('nofile'.encode('utf8'))
            continue
        num = os.stat(files).st_size
        conn.send(str(num).encode('utf8'))

        data = conn.recv(1024).decode('utf8')
        if data == 'num':
            fs = open(files,'rb')
            for line in fs:
                conn.send(line)
            fs.close()
    conn.close()



