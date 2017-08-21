#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-9 下午9:02'


import random

random_num = random.random()
print(random_num)

random_num_gt_int = random.uniform(0,9)
print(random_num_gt_int)


random_int = random.randint(0,10)
print(random_int)

random_range = random.randrange(1,9)
print(random_range)

list_src = [ 1,2,3,4,5,6,7,8,9 ]
random.shuffle(list_src)
print(list_src)

print(random.sample(list_src,2))


choice = ''

for i in range(4):
    num = random.randint(0,3)
    if i == num:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(1,9)
    choice +=str(tmp)
print(choice)