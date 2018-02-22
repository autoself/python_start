#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-18 上午8:59'





import socket
import json
import os

import sys



def uploadfile(cmd, cmdlist):
    if os.path.isfile(cmdlist[1]):
        client.send(cmd.encode('utf8'))
        cmd_ack = client.recv(1024).decode('utf8')
        #print(cmd_ack)
        fsize = os.stat(cmdlist[1]).st_size
        client.send(str(fsize).encode('utf8'))
        up_data = client.recv(1024).decode('utf8')
        if up_data != 'ack_ok_size':
            print('\033[31m  上传文件失败! \033[0m')
            return False
        fb = open(cmdlist[1], 'rb')
        send_size = 0
        for line in fb:
            client.send(line)
            send_size += len(line)
        fb.close()
        data = client.recv(1024).decode('utf8')
        print('\033[31m  上传文件成功!  \033[0m')
        return True
    else:
        print('\033[31m  请输入 upload file 文件不存在! \033[0m')
        return False


def donwloadfile(cmd,cmdlist):
    nowdir = os.path.join(os.getcwd(), 'download')
    if not os.path.isdir(nowdir):
        os.makedirs(nowdir)
    client.send(cmd.encode('utf8'))
    cmd_ack = client.recv(1024).decode('utf8')
    print(cmd_ack)
    if cmd_ack != 'cmd_ok':
        print('\033[31m  请输入 download file 格式! \033[0m')
        return False
    client.send('sync_ok'.encode('utf8'))
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
        if cmdlist[0] == 'upload':
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
            upload file   表示上传文件
            download file 表示下载文件 只是跟文件名
            '''
            print(info)
            continue




if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(('localhost',19999))
    run()


