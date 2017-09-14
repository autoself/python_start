#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-31 下午9:40'




def checkmax(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b,a+b
        n = n+ 1
    return 'done'

checkmax(10)
