#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-26 下午9:24'


import os
import sys

path_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path_dir)


from application import mangermain



if __name__ == '__main__':
    mangermain.run()