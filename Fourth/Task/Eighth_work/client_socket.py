#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-18 上午8:59'





import socket
import json
import os



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
                if os.path.isfile(cmdlist[1]):
                    client.send(cmd.encode('utf8'))
                    fsize = os.stat(cmdlist[1]).st_size
                    client.send(str(fsize).encode('utf8'))
                    up_data = client.recv(1024).decode('utf8')
                    fb = open(cmdlist[1],'rb')
                    send_size = 0
                    for line in fb:
                        client.send(line)
                        send_size += len(line)
                        print(send_size)
                    fb.close()
                    continue
                else:
                    print('\033[31m  请输入 upload file 文件不存在! \033[0m')
                    continue
            else:
                print('\033[31m  请输入 upload file 格式! \033[0m')
                continue
        else:
            info = '''
            ---------- 请参照下面帮助 ----------------
            ls            表示查询当前目录下的文件
            cd 目录       在当前家目录下进行切换其他目录
            upload file   表示上传文件
            download file 表示下载文件
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


