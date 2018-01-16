#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-16 下午2:45'



import socket


c = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c.connect(('localhost',9002))

if __name__ == '__main__':
    while True:

        cmd =  input('>>>')

        if not cmd : continue

        data =  cmd.split(' ')
        if len(data) != 2:
            print('Please get filename!!')
            continue
        if data[0] != 'get':
            print('Please get filename!!')
            continue

        # Send get filename
        c.send(cmd.encode('utf-8'))

        #return filename is not esxit
        rdata = c.recv(1024).decode('utf8')
        if rdata == 'nofile':
            print('nofile!!')
            continue
        print(rdata)
        c.send('num'.encode('utf8'))

        fs = open(data[1],'wb')
        resv_size = 0
        while resv_size < int(rdata):
            sfdata = c.recv(1024)
            resv_size += len(sfdata)
            fs.write(sfdata)
        else:
            fs.close()
            print('The end!')
