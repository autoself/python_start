#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-28 下午5:37'

import subprocess


data = subprocess.Popen('ls aaa' ,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

print(data.stdout.read().decode('utf-8'))
data.stdout.close()

#print(data.stderr.read().decode('utf-8'))
#data.stderr.close()