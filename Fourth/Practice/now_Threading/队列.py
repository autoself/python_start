#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-5 下午3:26'



import queue


q = queue.Queue()

q.put('a')
q.put('d')
q.put('c')




print(q.qsize())
print(q.get())
print(q.get())


d = queue.PriorityQueue()

d.put((1,'cca'))
d.put((3,'ccb'))
d.put((2,'ccc'))

print(d.get())
print(d.get())
print(d.get())