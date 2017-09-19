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

    def get_moot(self):
        print('this is moot: ',self.moot)

    def get_pri(self):
        print('this is __blood: ',self.__blood)


    def change_name(self,bask):
        print('change is bask: ', bask)
        self.moot = bask


a = Check_Obj('LiMing','18','AK1')
a.get_moot()
a.get_pri()
a.change_name('A8')

print(str(a._Role__blood))
a.get_moot()

