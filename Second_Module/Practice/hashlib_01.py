#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-15 下午1:12'


import  hashlib

hash = hashlib.md5('now'.encode(encoding='utf-8'))
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())


hash02 = hashlib.sha1('now'.encode(encoding='utf-8'))
hash02.update('admin'.encode(encoding='utf-8'))
print(hash02.hexdigest())

import hmac
h = hmac.new('now'.encode(encoding='utf-8'),msg='no1'.encode(encoding='utf-8'),digestmod='sha1')
h.update('admin'.encode(encoding='utf-8'))
print(h.hexdigest())