#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-11-20 下午9:57'



import socket


fclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
fclient.connect(('localhost',9008))

while True:
    cmd = input('Please>>>').strip()
    if len(cmd) == 0: continue
    if cmd.startswith('get'):
        fclient.send(cmd.encode())
        fsize = fclient.recv(1024)
        print('file size>>%s' % fsize)
        fclient.send('ack ok'.encode())
        resever_size = 0
        filename = cmd.split()[1]
        fc = open(filename + '.new','wb')
        while resever_size < int(fsize.decode()):
            data = fclient.recv(1024)
            resever_size +=len(data)
            fc.write(data)
        else:
            print('cmd res size ... %s' % resever_size)
        fc.close()