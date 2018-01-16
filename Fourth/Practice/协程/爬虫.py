#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-11 下午3:26'



import gevent

from  urllib.request import urlopen

import time

from gevent import monkey

monkey.patch_all()


def f(url):
    print('Get url %s' % url)
    rep = urlopen(url)
    data = rep.read()
    print('%d bytes received from %s.' % (len(data), url))






async_time = time.time()

gevent.joinall(
    [
        gevent.spawn(f,'http://sublimepython.top'),
        gevent.spawn(f, 'http://sublimepython.top'),
        gevent.spawn(f, 'http://sublimepython.top')
    ]
)

print('async:: ', time.time() - async_time )
