#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-5 下午9:02'



res = filter(lambda n:n>5,range(10))
res1 = [ i  for i in range(10) if i > 5 ]
for i in res:
    print(i)

for i in res1:
    print(i)

print("#"*50)
res = map(lambda n:n+1,range(10))   #   [ lambda n:n+1 for n in range(10) ]
res1 = [ n+1 for n in range(10) ]
res2 = [ lambda n:n+1 for n in range(10) ]
for i in res:
    print(i)
print("---"*30)
for i in range(len(res2)):
    print(res2[i](i))



import functools
res = functools.reduce(lambda x,y:x+y,range(10))
print(res)


dict_list = { 6:2 , 8:0, 1:4, -5:6, 99:11 , 4:22 }

print(sorted(dict_list.items(),key=lambda x:x[1]))


