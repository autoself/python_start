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


    def checkDatasize(self,user_limit_size,upload_file_size):
        '''
        获取目录下的所有文件的大小
        :param user_limit_size:用户限制多少
        :param upload_file_size: 上传的文件大小
        :return:
        '''

        #os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])  【文件夹路径, 文件夹名字, 文件名】

        allfiledir = os.walk(setting.USER_DIR)

        home_user_size = 0

        for root,dirs,filename in allfiledir:
            for file in filename:
                filedirs = os.path.join(root,file)
                home_user_size += os.stat(filedirs).st_size

        if ( int(upload_file_size) + home_user_size ) > int(user_limit_size):
             return False
        else:
            return True




    def uploadfile(self,cmd,username):
        '''
        上传文件的函数
        :param cmd: 传输的命令
        :return:
        '''
        print(cmd)
        userdir = os.getcwd()
        filename = os.path.basename(cmd[1])
        #print(filename)
        filesize = self.request.recv(1024)
        #print(filesize)
        #self.request.send('up_ok'.encode('utf8'))
        newdata = b''
        numlist = 0
        with open(setting.DB_FILE,'r',encoding='utf8') as fb:
            dbtable = json.load(fb)
        userlist_size = ''
        for key in dbtable:
            if dbtable[key]['username'] == username:
                userlist_size = dbtable[key]['disksize']
                break
        if not userlist_size or not filesize:
            self.request.send('size_faile'.encode('utf8'))
            return False
        else:
            check_status = self.checkDatasize(userlist_size,int(filesize.decode('utf8')))
            if check_status:
                self.request.send('size_ok'.encode('utf8'))
            else:
                self.request.send('size_faile'.encode('utf8'))
                return False
        try:
            fw = open(filename, 'wb')
            while numlist < int(filesize.decode('utf8')):
                data = self.request.recv(1024)
                numlist += len(data)
                fw.write(data)
            fw.close()
            self.request.send('finsh'.encode('utf8'))
            return True
        except:
            return False

    def downloadfile(self,cmd):
        '''
        进行下载文件
        :param cmd: 执行命令
        :return:
        '''
        userfile = os.getcwd() + os.sep + cmd[1]
        if os.path.isfile(userfile):
            self.request.send('up_ok'.encode('utf8'))
            filesize = os.stat(userfile).st_size
            data_ack_ok1 = self.request.recv(1024).decode('utf8')
            self.request.send(str(filesize).encode('utf8'))
            #print(filesize)
            data_ack_ok2 = self.request.recv(1024).decode('utf8')
            if data_ack_ok2:
                fb = open(userfile,'rb')
                for line in fb:
                    self.request.send(line)
                fb.close()
                return

        else:
            self.request.send('up_faild'.encode('utf8'))
            return False

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
            self.uploadfile(cmd,username)
        elif cmd[0] == 'download':
            self.downloadfile(cmd)



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