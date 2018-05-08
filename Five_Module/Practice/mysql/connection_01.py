#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-4-1 下午9:48'


import  MySQLdb

names = ["zhangsan","lisi","wangwu","zhaoliu",["libai","lihe","ligui","lishangyin"],"libai"]
names.insert(2,"dufu")         #插入元素
name2= [1,2,3,4]
names.extend(name2)            #扩展元素
names.append("libai")
