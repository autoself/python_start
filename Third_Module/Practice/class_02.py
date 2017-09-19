#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-19 上午9:29'



class Role(object):

    nationality = 'JP'

    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name = name
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.__heart = "Normal"

    def shot(self):
        print("%s is shooting..." % self.name)


    def got_shot(self):
        print("ah ..., I got shot ...")
        self.__heart = 'Die'
        print(self.__heart)

    def buy_gun(self,gun_name):
        print("%s just bought %s" % (self.name,gun_name) )
        self.weapon = gun_name


    def __del__(self):
        print('del run ....')


r1 = Role('Liming','ploice','Ak47')
# r2 = Role('Xiaoming','teacher','B22')
print(r1.got_shot())
# print(r1._Role__heart)
#
# print(r1.nationality)
# Role.nationality = 'SU'
#
# r1.nationality = 'CN'
# print(r1.nationality)
# print(r2.nationality)

#
# def shot2(self):
#     print('run my own shot method!',self.name)
#
# r1.shot = shot2
# r1.shot(r1)
# r2.shot()

