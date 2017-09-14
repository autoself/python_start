#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-5 上午8:31'


import shutil,os
import test_01

a = '/data/a'
c = '/data/c/a'
logger = test_01.logger('Test')
#shutil.copytree(a,c)
shutil.make_archive('/data/a','tar','/data/c',logger=logger.info('abc'))

import hashlib

a = hashlib.md5('abc'.encode('utf-8'))
a.update('ccs'.encode('utf-8'))
print(a.hexdigest())

from collections import deque

a = deque([])
a.append(1)
a.append(2)
a.pop()
print(a)

import hashlib
a = hashlib.md5()
print(a.hexdigest())
