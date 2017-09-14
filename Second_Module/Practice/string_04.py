#!/usr/bin/env python
#-*- coding:utf-8 -*-


__author__ = 'andylin'
__date__ = '17-9-6 下午8:50'



def a(func):
    print('aaa')
    func()
    print('bbb')
    return a

@a
def check_do():
    print('CCC')

def ABCD(abc):
    def check_login(func):
        def login(*args,**kwargs):
            print('AAA')
            print(abc)
            func(*args,**kwargs)
            print('BBBB')
        return login
    return check_login

DDD='CCCS'
@ABCD(abc=DDD)
def ABC():
    print('Success')

check_do
print("#"*30)
ABC()


import random



def change_code():
    check_num = []
    for i in range(2):
        random_num = random.randint(0, 9)
        a = random.randint(65, 90)
        b = random.randint(97, 122)
        random_upp = chr(a)
        random_low = chr(b)
        check_num.append(str(random_num))
        check_num.append(random_upp)
        check_num.append(random_low)
    code = ''.join(check_num)
    return code

code = change_code()
print(code)

from functools import reduce

a = filter(lambda x:x%2 == 0,range(1,101))
b = filter(lambda x:x%2 == 1,range(1,101))

nums = 0
b = 0
for i in range(0,50):
    a = b + 1
    b = a + 1
    nums = nums + a * b
print(nums)


def Change_num():
    checklist = []
    for i in range(2):
        a = random.randint(0,9)
        b = random.randint(65,90)
        c = random.randint(97,122)
        checklist.append(str(a))
        checklist.append(chr(b))
        checklist.append(chr(c))
    random.shuffle(checklist)
    strs = ''.join(checklist)
    return strs
nu = Change_num()
print(nu)