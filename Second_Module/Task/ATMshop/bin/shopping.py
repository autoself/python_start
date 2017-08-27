#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-27 下午12:44'



import os
import sys

path_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path_dir)

'''
简单实现 购物买所有物品后,结束购物时结涨
'''

from application import shoppingmain


if __name__ == '__main__':
    shoppingmain.run()

