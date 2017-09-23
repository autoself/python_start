#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-21 下午4:02'


class ABC(object):

    def __init__(self):
        self.data  = {}

    def __getitem__(self, item):
        print('__getitem__',item)
        return self.data.get(item)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)
        self.data[key] = value

    def __delitem__(self, key):
        print('__delitem__',key)


d = ABC()
d['name'] = 'Liming'
print(d['name'])
del d['name']