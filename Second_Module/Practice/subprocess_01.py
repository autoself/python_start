#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-16 下午5:48'


import subprocess


print(subprocess.call(['echo','aaaa'],shell=False))
print(subprocess.call(['echo','aaaas'],shell=True))

print("#"*50)
print(subprocess.check_call(['echo','ccc'],shell=False))
print(subprocess.check_call(['echo','cccs'],shell=True))

print("-"*30)
print(subprocess.check_output(['echo','hello world']))
print(subprocess.check_output(['echo','hello world'],shell=True))

print("!"*30)

print(subprocess.Popen(['echo','CCCS']))
print(subprocess.Popen(['echo','CCCS'],shell=True))

print("+"*50)
print(subprocess.Popen(['echo','aacs'],shell=True,cwd='/root'))



print(subprocess.PIPE)