#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-19 下午4:38'



class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print('pession is talking...')


class BlackPersion(Person):
    def __init__(self,name,age):
        #super(Person,self).__init__(name,age)
        Person.__init__(self,name,age)

    def talk(self):
        print('black persion ...')


a1 = BlackPersion('Liming',16)


