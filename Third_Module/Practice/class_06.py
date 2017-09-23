#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-22 上午10:07'


class MyType(type):

    def __init__(self,what,bases=None,dict=None):
        super(MyType,self).__init__(what,bases,dict)

    def __call__(self, *args, **kwargs):
        print('__call__')
        obj = self.__new__(self,*args, **kwargs)
        self.__init__(obj,*args,**kwargs)


class Foo(object):

    __metaclass__ = MyType

    def __init__(self,name):
        self.name = name
        print('Foo --init--')


    def __new__(cls, *args, **kwargs):
        print('Foo __new__')
        return object.__new__(cls)

obj = Foo('Liming')