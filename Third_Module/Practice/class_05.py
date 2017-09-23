#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-21 下午5:10'

#
# class Foo(object):
#     def __init__(self,name):
#         self.name = name
#
#
# f = Foo('alex')
# print(type(f))
# print(type(Foo))


def func(self):
    print('hello Alex')


Foo = type('Foo',(),{'func':func})


a = Foo()
a.func()