#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-26 下午2:35'


import socket
import json
import re, os
import struct
import hmac

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class FtpClient(object):
    '''
     ftp连接的客户端
    '''

    def __init__(self,host,port,username,password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.path = os.path.join(BASE_DIR, 'download')

    def Auth_login(self,Fclient):
        paswd = hmac.new(bytes(self.password,encoding='utf-8'),b'abc')
        checkdata = json.dumps({'username': self.username, 'password': paswd.hexdigest()})
        Fclient.send(checkdata.encode('utf-8'))
        auth_login = Fclient.recv(1024)
        return auth_login

    def ClientBind(self):
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
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

            data_str = re.split('\s+',data)
            if data_str[0] == 'upload':
                if len(data_str) == 2:
                    if os.path.isfile(data_str[1]):
                        Fclient.send(data.encode('utf-8'))
                        fs = open(data_str[1],'r',encoding='utf-8')
                        fsrd = fs.read().encode('utf-8')
                        inputlen = len(fsrd)
                        datanum = struct.pack('i',inputlen)
                        Fclient.send(datanum)
                        while inputlen > 0:
                            readlen = 1024
                            if inputlen < readlen:
                                readlen = inputlen
                            Fclient.send(fsrd[:readlen])
                            inputlen -=readlen
                            fsrd = fsrd[readlen:]
                        fs.close()
                        rdata = Fclient.recv(1024).decode('utf-8')
                        print(rdata)
                        continue
                    else:
                        print('this is not file!!')
                        continue
                else:
                    print('Please enter the correct command,Please command [help]')
                    continue
            elif data_str[0] == 'download':
                if len(data_str) == 2:
                    Fclient.send(data.encode('utf-8'))
                    newfile = os.path.join(self.path,os.path.basename(data_str[1]))
                    nums = Fclient.recv(4)
                    fileLen = struct.unpack('i', nums)[0]
                    outfile = open(newfile, 'w')
                    datanow = b''
                    while fileLen > 0:
                        readLen = 1024
                        if fileLen < readLen: readLen = fileLen
                        data = Fclient.recv(readLen)
                        datanow = datanow + data
                        fileLen -= readLen
                    outfile.write(datanow.decode('utf-8'))
                    outfile.close()
                    rdata = Fclient.recv(1024).decode('utf-8')
                    print(rdata)
                    continue
                else:
                    print('Please enter the correct command,Please command [help]')
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
    #username = 'abc'
    #password = 'abc123'
    fc = FtpClient(host,port,username,password)
    fc.ClientBind()