#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-9 上午9:18'



from multiprocessing import Process, Queue
import time
import os

def Product(q2):
    count = 0
    while True:
        q2.put( '生产出 %s' % count)
        print('product pid %s %s' % (os.getpid(),count))
        count += 1


def Comment(q2,name):
    while True:
        print('%s start pid:%s --- %s' %(name,os.getpid(),q2.get()))
        time.sleep(1)

if __name__  == '__main__':
    q = Queue(maxsize=5)
    p = Process(target=Product,args=(q,))
    c = Process(target=Comment, args=(q,'Alex'))
    d = Process(target=Comment, args=(q, 'bill'))

    p.start()
    c.start()
    d.start()

