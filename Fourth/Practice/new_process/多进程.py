#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-8 下午5:17'



import multiprocessing
import time

def Run(name):
    time.sleep(2)
    print('hello %s' % name )

if __name__ == '__main__':

    processlist = []
    for i in range(10):
        p = multiprocessing.Process(target=Run,args=('Alex',))
        p.start()
        processlist.append(p)

    for p in processlist:
        p.join()
    #p.join()