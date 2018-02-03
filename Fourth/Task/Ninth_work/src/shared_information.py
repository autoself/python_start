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
        except:
            return False
        finally:
            return data
    else:
        return False




def ssh_connect(hostname,username,password,port,commond):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=hostname,username=username,password=password,port=int(port),timeout=10)
    stdin,stdout,stderr = ssh.exec_command(commond)
    result = stdout.read()
    print(result)
    ssh.close()



def ssh_download()

