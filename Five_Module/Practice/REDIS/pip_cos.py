#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-3-24 下午9:09'


import redis


pool = redis.ConnectionPool(host='127.0.0.1',port=6379)

r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

r.set('name','andylin')
r.set('name1','abc')

pipe.execute()