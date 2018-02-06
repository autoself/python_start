#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-2-3 下午3:12'


import os
from etc import setting
import json
import paramiko

def read_machine():
    '''
    读取表信息
    :return:
    '''
    if os.path.isfile(setting.DB_USER):
        try:
            with open(setting.DB_USER,'r',encoding='utf8') as fr:
                data = json.load(fr)
            return data
        except:
            return False
    else:
        return False



def group_machine():
    '''
        读取数据组
        :return:
        '''
    if os.path.isfile(setting.DB_GROUP):
        try:
            with open(setting.DB_GROUP, 'r', encoding='utf8') as fr:
                data = json.load(fr)
            return data
        except:
            return False
    else:
        return False




def __ssh_connect(hostname,username,password,port):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname=hostname, username=username, password=password, port=int(port), timeout=2)
        return ssh
    except:
        print("\033[31;1m%s连接失败！请检查原因\033[0m" % hostname)
        return False



def ssh_command(hostname,username,password,port,commond):
    ssh = __ssh_connect(hostname,username,password,port)
    if not ssh:
        return False
    try:
        stdin,stdout,stderr = ssh.exec_command(commond)
        result = stdout.read()
        print(result)
        ssh.close()
        return True
    except:
        return False


def __ssh_scp(hostname,username,password,port):
    try:
        transport = paramiko.Transport(sock=(hostname,int(port)))
        transport.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp
    except:
        print("\033[31;1m%s连接失败！请检查原因\033[0m" % hostname)
        return False




def ssh_download(hostname,username,password,port,remote_file,local_file):
    ssh = __ssh_scp(hostname,username,password,port)
    if not ssh:
        return False
    try:
        ssh.get(remote_file,local_file)
    except:
        print('下载文件失败！')
        return False
    finally:
        print('%s下载成功！' % hostname)
        ssh.close()
        return True


def ssh_upload(hostname,username,password,port,remote_file,local_file):
    ssh = __ssh_scp(hostname,username,password,port)
    if not ssh:
        return False
    try:
        ssh.put(local_file,remote_file)
    except:
        print('上传文件失败！')
        return False
    finally:
        print('%s上传文件成功！'% hostname)
        ssh.close()
        return True