#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-26 下午2:35'


import socket
import json

class FtpClient(object):
    '''
     ftp连接的客户端
    '''

    def __init__(self,host,port,username,password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def Auth_login(self,Fclient):
        checkdata = json.dumps({'username': self.username, 'password': self.password})
        Fclient.send(checkdata.encode('utf-8'))
        auth_login = Fclient.recv(1024)
        return auth_login

    def ClientBind(self):

        Fclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        Fclient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            Fclient.connect((self.host,self.port))
        except:
            return False


        check_login = self.Auth_login(Fclient)
        if check_login:
            print('You are welcome to login successfully!')
        else:
            print('Authentication failed!')
            Fclient.close()
            return False


        while True:
            data = input('>>>>').strip()
            if not data:
                continue
            Fclient.send(data.encode('utf-8'))
            rdata = Fclient.recv(1024).decode('utf-8')
            if rdata:
                print(rdata)
            else:
                continue
        Fclient.close()

if __name__ == '__main__':

    host = 'localhost'
    port = 6969
    username = input("username:")
    password = input("password:")
    fc = FtpClient(host,port,username,password)
    fc.ClientBind()