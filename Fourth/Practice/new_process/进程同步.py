#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-10 上午10:56'

from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()