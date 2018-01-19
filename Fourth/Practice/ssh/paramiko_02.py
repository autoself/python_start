#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-17 上午10:55'


import paramiko

transport = paramiko.Transport(('localhost',22))
transport.connect(username='root',password='mango')

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('/root/log.txt','/mnt/log.txt')

transport.close()