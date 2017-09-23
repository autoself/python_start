#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-9-20 下午5:41'


class Dog(object):
    name = 'Huiwei'
    def __init__(self, name):
        self.name = name

    @staticmethod  # 把eat方法变为静态方法
    def eat(self):
        print("%s is eating" % self )

    @classmethod
    def talk(cls):
        print('%s is talk!' % cls.name)


    @property
    def out(self):
        print('%s is files' % self.name )

    @out.setter
    def out(self,food):
        print('%s  eat %s' % (self.name,food) )
        self.name = food

    @out.deleter
    def out(self):
        print('del food')
        del self.name

d = Dog("ChenRonghua")
d.eat('Liming')

d.talk()

#d.out
d.out = 'apple'
d.out
del d.out