#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-24 下午11:04'

import os
import sys

path_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path_dir)


from application import atmmain



if __name__ == '__main__':
    atmmain.run()