#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-25 上午11:03'


import socket
import os
import sys
import json
import re
import struct

import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



class FtpServer(object):
    '''
       Disction Ftp Server Socket!
    '''

    def __init__(self, host, port):
        '''
        Fictitious function

        :param ip:   server ip
        :param port: server port
        '''
        self.host = host
        self.port = port
        self.userfile = os.path.join(BASE_DIR,'user','user.json')
        self.username= ''
        self.home = 'home'
        self.commandlist = {'ls':self.List_dir,'rm':self.Rm_file,'upload':self.Upload_file,'download':self.Download_file,'help':self.Help_list}

    def LoginCheck(self,*args,**kwargs):
        '''
        主要是检查用户是否认证登录
        :param args:
        :param kwargs:
        :return:
        '''
        with open(self.userfile,'r',encoding='utf-8') as fs:
            sqldata = json.load(fs,encoding='utf-8')
        if kwargs['username'] in sqldata:
            if sqldata[kwargs['username']] == kwargs['password'] :
                userhome = os.path.join(BASE_DIR,self.home,kwargs['username'])
                if not os.path.exists(userhome):
                    os.makedirs(userhome)
                self.username = kwargs['username']
                return True
        return False


    def Help_list(self,datalist):
        data = '''
        ls               --View current file
        rm [file]        --Delete file
        upload [file]    --Upload files
        download [file]  --Download File
        '''.encode('utf-8')
        return data

    def List_dir(self,datalist):
        ospath = os.path.join(BASE_DIR, self.home, self.username)
        os.chdir(ospath)
        command = re.split('\s+', datalist)
        if len(command) > 1:
            status = b'Please enter the correct command,Please command [help]'
            return status
        stdata = subprocess.Popen(datalist,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True,cwd=ospath)
        data = stdata.stdout.read()
        stdata.stdout.close()
        if not data:
            data = stdata.stderr.read()
            stdata.stderr.close()
        if not data:
            data = b'There are no files in the current directory'
        return data

    def Rm_file(self,datalist):
        ospath = os.path.join(BASE_DIR, self.home, self.username)
        os.chdir(ospath)
        command = re.split('\s+', datalist)
        if len(command) != 2:
            status = b'Please enter the correct command,Please command [help]'
            return status
        if not os.path.isfile(command[1]):
            status = b'The file you deleted is not a file!'
            return status
        stdata = subprocess.Popen(datalist, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=ospath)
        status = b'The file you deleted file Success!'
        return status


    def Upload_file(self,fconn, datalist):
        ospath = os.path.join(BASE_DIR, self.home, self.username)
        os.chdir(ospath)
        command = re.split('\s+', datalist)
        newfile = os.path.basename(command[1])
        nums = fconn.recv(4)
        fileLen = struct.unpack('i',nums)[0]
        print(fileLen)
        outfile = open(newfile,'w')
        datanow = b''
        while fileLen > 0:
            readLen = 1024
            if fileLen < readLen: readLen = fileLen
            data = fconn.recv(readLen)
            datanow = datanow + data
            fileLen -= readLen
        outfile.write(datanow.decode('utf-8'))
        outfile.close()
        status = b'The file you upload file Success!'
        return status


    def Download_file(self,fconn,datalist):
        ospath = os.path.join(BASE_DIR, self.home, self.username)
        os.chdir(ospath)
        command = re.split('\s+', datalist)
        newfile = os.path.basename(command[1])
        if os.path.isfile(newfile):
            fs = open(newfile, 'r', encoding='utf-8')
            fsrd = fs.read().encode('utf-8')
            inputlen = len(fsrd)
            print(inputlen)
            datanum = struct.pack('i', inputlen)
            fconn.send(datanum)
            while inputlen > 0:
                readlen = 1024
                if inputlen < readlen:
                    readlen = inputlen
                fconn.send(fsrd[:readlen])
                inputlen -= readlen
                fsrd = fsrd[readlen:]
            fs.close()
            status = b'The file you download file Success!'
        else:
            status = b'The file does not exist'
        return status


    def System_write(self, fconn,data):
        command = re.split('\s+', data)
        if command[0] in self.commandlist:
            if command[0] =='upload':
                check_data = self.commandlist[command[0]](fconn,data)
            elif command[0] == 'download':
                check_data = self.commandlist[command[0]](fconn, data)
            else:
                check_data = self.commandlist[command[0]](data)
            return check_data
        else:
            status = b'Please enter the correct command,Please command [help]'
            return status

    def SockBind(self):
        '''
        开启socket
        :return:
        '''
        #AF_INET:开启ipv4, SOCK_STREAM:TCP形式
        fserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        fserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            fserver.bind((self.host,self.port))
        except:
            raise '启动败!请检查是否端口被占用'
        fserver.listen()

        while True:
            fconn,faddr = fserver.accept()
            checkdata = fconn.recv(1024).decode('utf-8')
            if not checkdata:
                fconn.close()
                return False

            #首次调用认证
            userpass = json.loads(checkdata)
            auth_login = self.LoginCheck(**userpass)
            if not auth_login:
                fconn.send(b'')
                fconn.close()
                continue
            fconn.send(b'True')

            while True:
                data = fconn.recv(1024).decode('utf-8')
                if not isinstance(data, str):
                    break
                if data:
                    datas = self.System_write(fconn,data)
                    fconn.send(datas)
                else:
                    fconn.send(b'')
                    break
            fconn.close()
        fserver.close()
        return True

def startlogin():
    '''
    相当于数据库一样,只是用json存储
    :return:
    '''
    logindir = os.path.join(BASE_DIR,'user')
    logfile = os.path.join(logindir,'user.json')
    if not os.path.exists(logindir):
        os.makedirs(logindir)
    if os.path.isfile(logfile):
        return True
    defaultusername = {'abc':'abc123','liming':'abc123'}
    try:
        with open(logfile,'w',encoding='utf-8') as fs:
            json.dump(defaultusername,fs)
    except :
        raise 'User file IOerror!'
    return True


if __name__ == '__main__':
    startlogin()
    ftpcl = FtpServer('localhost',6969)
    ftpcl.SockBind()