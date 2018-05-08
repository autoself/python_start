#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-3-24 下午4:42'

import redis

r = redis.Redis(host='127.0.0.1',port=6379)
r.set('foo','bar')
print(r.get('foo'))