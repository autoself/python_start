#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-18 上午8:59'




import socketserver
import hmac
import os
import json
import subprocess



import  sys

BASEDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEDIR)

from etc import setting





class MySocketServer(socketserver.BaseRequestHandler):


    def login(self,userpwd):
        '''
        主要是检测是否登录
        :param userpwd: 用户与密码 字典
        :return:
        '''
        if os.path.isfile(setting.DB_FILE):
            with open(setting.DB_FILE,'r',encoding='utf8') as fb:
                dbtable = json.load(fb)
            for key in dbtable:
                if dbtable[key]['username'] == userpwd['username']:
                    pwd = hmac.new(userpwd['password'].encode('utf8'),setting.DB_PWD_MD5.encode('utf8'))
                    if dbtable[key]['password'] == pwd.hexdigest():
                        return userpwd['username']
        return False


    def changeuserdir(self,cmd,username):
        '''
        对目录进行切换动作
        :param cmd:        传入的命令
        :param username:   用户名
        :return:
        '''
        viewdir = subprocess.Popen('%s' % (' '.join(cmd)), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        dataerr = viewdir.stderr.read()
        dataout = viewdir.stdout.read()
        chagedir = os.path.join(setting.USER_DIR, username)
        olddir = os.getcwd()
        if not dataerr and not dataout:
            os.chdir(cmd[1])
            nowdir = os.getcwd()
            if chagedir in nowdir:
                self.request.send('sync_ok'.encode('utf8'))
                return True
            else:
                os.chdir(olddir)
                self.request.send('sync_err'.encode('utf8'))
                return False
        else:
            os.chdir(olddir)
            self.request.send('sync_err'.encode('utf8'))
            return False

    def uploadfile(self,cmd):
        '''
        上传文件的函数
        :param cmd: 传输的命令
        :return:
        '''
        userdir = os.getcwd()
        filename = os.path.basename(cmd[1])
        #print(filename)
        filesize = self.request.recv(1024)
        #print(filesize)
        self.request.send('up_ok'.encode('utf8'))
        fw = open(filename,'wb')
        newdata = b''
        numlist = 0
        while numlist < int(filesize.decode('utf8')):
            data = self.request.recv(1024)
            numlist += len(data)
            fw.write(data)
        fw.close()

    def run(self,data,username):
        cmd = data.decode('utf8').split()
        if cmd[0] == 'ls':
            userdir = os.getcwd()
            viewls  = subprocess.Popen('ls %s' % (userdir),shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
            data = viewls.stdout.read()
            if not data :
                self.request.send('empty file'.encode('utf8'))
            else:
                self.request.send(data)
        elif cmd[0] == 'cd':
            self.changeuserdir(cmd,username)
        elif cmd[0] == 'upload':
            self.uploadfile(cmd)







    def handle(self):
        conn = self.request
        userpwd = json.loads(conn.recv(1024).decode('utf8'))
        if not userpwd: return False
        check_login = self.login(userpwd)
        chagedir = os.path.join(setting.USER_DIR,userpwd['username'])
        if not check_login or not os.path.isdir(chagedir):
            conn.send(str('False').encode('utf8'))
            return False
        else:
            os.chdir(chagedir)
            conn.send(str('True').encode('utf8'))
        while True:
            data = conn.recv(1024)
            if not data: break
            self.run(data,check_login)





if __name__ == '__main__':

    HOST = '127.0.0.1'
    PORT = 9999

    # 表示开启当服务器挂了,会立刻释放tcp
    socketserver.TCPServer.allow_reuse_address = True

    # 监听10000个线程
    socketserver.TCPServer.request_queue_size = 10000

    server = socketserver.ThreadingTCPServer((HOST,PORT),MySocketServer,bind_and_activate=True)


    server.serve_forever()