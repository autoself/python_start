#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-13 下午8:17'


import re



a = re.search('(\d{4})',"331424199009200359")
print(a.group())

#shutil.make_archive
b = re.findall('\D+','abcd1213dafasf232cs2-')
c = re.findall('\d+','abcd1213dafasf232cs2')
print(b)
print(c)



print(re.findall('\d+','asdfa234123lklasdfk234lkasdf31l'))

