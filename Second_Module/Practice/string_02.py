#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-30 上午9:20'

import collections



class A:
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print('hello',self.name)

aa = A('xiaomi')

print(aa.__getattribute__('name'))

a1 = '+1+1'
print(a1.rsplit('+',1))
print(a1.rpartition('+'))

a2 = 'abCdEf'
print(a2.upper())
print(a2.lower())
if a2.islower():
    print("abc is True")
else:
    print("abc is False")

a3 = ' '
a4='四'
a5 = 'acbDef'
print(a2.isalnum())
print(a2.isalpha())
print(a4.isnumeric())
print(a4.isdigit())
print(a4.center(40,'#'))
print(a5.casefold())
print(a5.count('e'))

d = {'stu1102': 'LongZe Luola', 'stu1103': 'XiaoZe Maliya', 'stu1101': '武藤兰'}

del d['stu1103']
print(d)

def f(a):
    a.append(5)


b = [ 2,3,4 ]
f(b)
print(b)

def f1(a):
    b = {1:2}
    a.update(b)

c = { 'a':'b' }
f1(c)
print(c)

def f2(a):
    a.update([1,2,3])

s = set([4,5,6])
f2(s)
print(s)

b = set([23,2,45])
s.add(9)
print(s)

print(s.difference(b))
print(s.symmetric_difference(b))

print(s.union(b))

import collections

a = 'aaabbbcccddd'
c = {}
print(collections.Counter(a))
d = collections.OrderedDict(c)
d['x'] = 1
d['y'] = 2
d['a'] = 3
print(d)
d1 = [ 1,2,3,4 ]
dd = collections.deque(d1)
dd.append(5)
print(dd)
print(lambda :'N/A')
d3 = collections.defaultdict('a')
print(d3['key1'])