#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-2-6 下午9:12'

import selectors
import socket
import os

global_select = selectors.DefaultSelector()


def accept(ser, mask):
    conn, addr = ser.accept()  # Should be ready
    cmd = conn.recv(1024)  # Should be ready
    print(cmd)
    if cmd:
        cmdlist = cmd.decode('utf8').split()
        if cmdlist[0] == 'upload':
            status_check = upload_file(conn, cmdlist)
        elif cmdlist[0] == 'download':
            status_check = download_file(conn,cmdlist)
        else:
            conn.send('cmd_not'.encode('utf8'))
    else:
        conn.close()


def upload_file(conn,cmd):
    '''
     上传文件的函数
     :param cmd: 传输的命令
     :return:
    '''
    conn.send('cmd_ok'.encode('utf8'))
    upload_dir = os.path.join(os.getcwd(),'uploadfile')
    if not os.path.isdir(upload_dir):
        os.makedirs(upload_dir)
    filename = os.path.basename(cmd[1])
    uploadfile = os.path.join(upload_dir,filename)
    filesize = conn.recv(1024).decode('utf8')
    ack_size = conn.send('ack_ok_size'.encode('utf8'))
    recv_size = 0
    fw = open(uploadfile, 'wb')
    try:
        while recv_size < int(filesize):
            data = conn.recv(1024)
            recv_size += len(data)
            fw.write(data)
        fw.close()
        return True
    except:
        return False

def download_file(conn,cmdlist):
    filename = os.path.basename(cmdlist[1])
    donwload_filename = os.path.join(os.getcwd(),'uploadfile',filename)
    if os.path.isfile(donwload_filename):
        conn.send('cmd_ok'.encode('utf8'))
    else:
        conn.send('cmd_not'.encode('utf8'))
    sync = conn.recv(1024).decode('utf8')
    file_size = os.stat(donwload_filename).st_size
    conn.send(str(file_size).encode('utf8'))
    sync_ack = conn.recv(1024).decode('utf8')
    print(sync_ack)
    fb = open(donwload_filename, 'rb')
    send_size = 0
    for line in fb:
        conn.send(line)
    fb.close()
    conn.close()







if __name__ == '__main__':
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('localhost', 19999))
    server.listen(10000)
    server.setblocking(False)
    global_select.register(server, selectors.EVENT_READ, accept)


    while True:
        events = global_select.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)



