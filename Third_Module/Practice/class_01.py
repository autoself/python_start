#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-14 上午9:43'



class Check_Obj(object):
    def __init__(self,name,age,moot):
        self.name = name
        self.age = age
        self.moot = moot
        self.__blood = 100

        