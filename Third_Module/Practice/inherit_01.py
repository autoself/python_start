#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-19 下午4:38'

class Persons(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class BlackPersion(Persons):
    def __init__(self, name ,age):
        super(BlackPersion,self).__init__(name,age)

    def talk(self):
        print('black persion ...')


a1 = BlackPersion('Liming',18)

a1.talk()