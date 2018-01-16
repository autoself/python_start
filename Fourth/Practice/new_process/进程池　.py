#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-10 上午11:16'

from multiprocessing import Process, Pool

import time

def f(num):
    print('process %s' % num)
    time.sleep(2)
    return num + 100

def bak(arg):
    print('--> exec done: ',arg )


if __name__ == '__main__':
    a = Pool(processes=5)
    for i in range(10):
        a.apply_async(func=f, args=(i,), callback=bak)

    print('end')
    a.close()
    a.join()