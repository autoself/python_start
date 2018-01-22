#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-18 上午8:59'





import socket
import json
import os

import sys

def login():
    username = input('请输入ftp用户名>>>')
    password = input('请输入ftp密码>>>')

    data = json.dumps({'username':username,'password':password}).encode('utf8')

    client.send(data)

    rdata = client.recv(1024).decode('utf8')
    if rdata == 'True':
        print('\033[32m------------ 登录 Ftp 成功 --------------\033[0m')
        run()
    else:
        print('\033[31m 账号或密码错误! \033[0m')
        return False


def uploadfile(cmd, cmdlist):
    if os.path.isfile(cmdlist[1]):
        client.send(cmd.encode('utf8'))
        fsize = os.stat(cmdlist[1]).st_size
        client.send(str(fsize).encode('utf8'))
        up_data = client.recv(1024).decode('utf8')
        if up_data != 'size_ok':
            print('\033[31m  上传文件失败,有限制大小! \033[0m')
            return False
        fb = open(cmdlist[1], 'rb')
        send_size = 0
        for line in fb:
            client.send(line)
            send_size += len(line)
        fb.close()
        data = client.recv(1024).decode('utf8')
        return True
    else:
        print('\033[31m  请输入 upload file 文件不存在! \033[0m')
        return False


def donwloadfile(cmd,cmdlist):
    nowdir = os.path.join(os.getcwd(), 'download')
    if not os.path.isdir(nowdir):
        os.makedirs(nowdir)
    client.send(cmd.encode('utf8'))
    file_status = client.recv(1024).decode('utf8')
    if file_status != 'up_ok':
        print('\033[31m  请输入 download file 格式! \033[0m')
        return False
    client.send('ack_ok'.encode('utf8'))
    file_size = client.recv(1024).decode('utf8')
    client.send('ack_ok'.encode('utf8'))
    filename = os.path.join(nowdir, cmdlist[1])
    fw = open(filename, 'wb')
    recv_size = 0
    try:
        while recv_size < int(file_size):
            data = client.recv(1024)
            recv_size += len(data)
            fw.write(data)
            # 进度条
            rate = recv_size / int(file_size)
            rate_num = int(rate * 100)
            ## %% 百分号标记  %d 有符号整数(十进制)  %s==>字符串
            ## %[(name)][flags][width].[precision]typecode
            ## - 左对齐；正数前无符号，负数前加负号；
            ## + 右对齐；正数前加正好，负数前加负号；
            ## %-100s 表示右边不够的则用空格填充
            r = '\r[%-100s]%d%%' % ('>' * rate_num, rate_num,)
            sys.stdout.write(r)
            print()
            sys.stdout.flush()
        fw.close()
        return True
    except:
        return False


def run():
    while True:
        cmd = input('>>>').strip()
        if not cmd : continue
        cmdlist = cmd.split(' ')
        if cmdlist[0] == 'ls':
            if len(cmdlist) == 1:
                client.send(cmd.encode('utf8'))
                data = client.recv(1024)
                print(data.decode('utf8'))
            else:
                print('\033[31m  输入的ls 不能带任何参数！ \033[0m')
                continue
        elif cmdlist[0] == 'cd':
            if len(cmdlist) == 2:
                client.send(cmd.encode('utf8'))
                cd_data = client.recv(1024).decode('utf8')
                if cd_data == 'sync_err':
                    print('\033[31m  切换目录失败!请在家目录中切换! \033[0m')
                continue
            else:
                continue
        elif cmdlist[0] == 'upload':
            if len(cmdlist) == 2:
                uploadfile(cmd, cmdlist)
                continue
            else:
                print('\033[31m  请输入 upload file 格式! \033[0m')
                continue
        elif cmdlist[0] == 'download':
            if len(cmdlist) == 2:
               donwloadfile(cmd,cmdlist)
               continue
            else:
                print('\033[31m  请输入 download file 格式! \033[0m')
                continue
        else:
            info = '''
            ---------- 请参照下面帮助 ----------------
            ls            表示查询当前目录下的文件
            cd 目录       在当前家目录下进行切换其他目录
            upload file   表示上传文件
            download file 表示下载文件 只是跟文件名
            '''
            print(info)
            continue




if __name__ == '__main__':
    HOST = '127.0.0.1'
    POST = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect((HOST, POST))
    login()


