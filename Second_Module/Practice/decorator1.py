#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-1 下午9:49'



import time


def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("the func run time is %s" % (stop_time - start_time))
    return deco


@timer
def test1():
    time.sleep(1)
    print("in the test1")

test1()