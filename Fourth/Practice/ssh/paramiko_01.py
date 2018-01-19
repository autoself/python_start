#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-17 上午10:17'



import paramiko


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

ssh.connect(hostname='192.168.23.128',port = 22,username='root',password='mango')

stdin,stdout,stderr = ssh.exec_command('df')

result = stdout.read()

print(result)

ssh.close()