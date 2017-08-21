#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-5 下午4:53'

from itertools import islice

class checkFunc(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        value = self.a
        self.a += self.b
        self.b = value
        return value

f = checkFunc(2,3)
print(list(islice(f,0,10)))