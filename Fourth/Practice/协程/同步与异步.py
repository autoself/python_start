#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-11 下午3:22'

import gevent


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(0.5)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
