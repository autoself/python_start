#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-29 下午7:21'



a = '12345678'

b = {1:'a',2:'b'}

c = {'1':'a','2':'b'}
d='1'
h =[ 1,2,3,4,5,6 ]
#print(dir(a))
aa = 'a b'
e=''

print(a.__add__('9')) #结果 123456789
print(a.__class__)
print(a.__contains__('1'))  #表示 是否在字符串中, 如果是返回 True
print(a.__eq__('12345678')) #表示是否相等，相等返回True
print(a.__ge__('1'))        #表示是否大于等于，如果是就True

print('{0}'.format(4))

#from datetime import date
#d = date.today()
#format = "%b %d %Y"
#print(d.__format__(format))


print(a.__len__())
print('{name}'.format(name='aa'))

'''
Background:

format(obj, fmt) eventually calls object.__format__(obj, fmt) if obj (or one of its bases) does not implement __format__. The behavior of object.__format__ is basically:

def __format__(self, fmt):
    return str(self).__format__(fmt)
'''

print( str('1+1j').__format__('10s'))  #多了很多空格

#format()  ==  __format__
#print(a.__getattribute__())
print(a.__getitem__(1))     #获取 a[1]

#name='1'

#c.__delattr__(name)
#print(c[name])
print(abs(-1))  #返回一个数的绝对值。参数可以是普通的整数，长整数或者浮点数。如果参数是个复数，返回它的模。
print(all([0,1,2,3]))   #如果iterable,可迭代对象 的所有元素为真（或者iterable为空）， 返回True
                #如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；


print(any([0]))  # 如果iterable的任一元素为真，返回True。如果iterable为空，返回False。等同于：
print(bin(12))  # 0b1100 将一个整数转化成一个二进制字符串。结果是一个合法的Python表达式。如果x不是一个Python int对象，它必须定义一个返回整数的__index__()方法。
print(bytearray(a,encoding='utf-8'))

print(chr(67))   # C
print(ord('C'))  # 67

str01 = "for i in range(2): print(i)"
print(exec(compile(str01,'','exec')))   #compile(source, filename, mode[, flags[, dont_inherit]])

print(complex('2+1j'))
l = [1, 3, 4, 5]
for i in l:
    print(complex(i, 5))        # 复数


class A:
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print('hello',self.name)

aa = A('xiaomi')
print(delattr(aa,'name'))           #这个函数和setattr()有关。参数是一个对象和一个字符串。字符串必须是对象的某个属性的名字。只要对象允许，这个函数删除该名字对应的属性。

print(aa.__getattribute__('name'))

print(divmod(1,2))      #返回商和余数的二元组

print(list(enumerate(a)))#返回一个枚举对象。sequence必须是序列或迭代器iterator，或者支持迭代的对象。

ac = filter(lambda x:x%2 == 1 ,list(range(10)))
print( [i for i in ac ] )

ac = map(lambda x:x+2,list(range(10)))
print( [i for i in ac ] )

from functools import reduce
ac = reduce(lambda x,y:x+y, list(range(10)))
print(ac)


print(frozenset(a))      #不可改变的

print(round(1.2222,3))
print(pow(2,2))
print(sum([20,23]))
print('aaA\ta'.expandtabs(8))
print(callable(a))
print(callable(A))