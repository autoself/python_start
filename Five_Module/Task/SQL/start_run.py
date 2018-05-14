#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-5-11 下午10:20'


from os import path
import sys

BASEHOME = path.dirname(path.abspath(__file__))
sys.path.append(BASEHOME)

from src import manager


if __name__ == '__main__':
    manager.run()