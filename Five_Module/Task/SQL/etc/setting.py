#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-5-8 下午9:59'

'''
用户角色，讲师＼学员， 用户登陆后根据角色不同，能做的事情不同，分别如下
讲师视图
　　管理班级，可创建班级，根据学员qq号把学员加入班级
　　可创建指定班级的上课纪录，注意一节上课纪录对应多条学员的上课纪录， 即每节课都有整班学员上， 为了纪录每位学员的学习成绩，需在创建每节上课纪录是，同时 为这个班的每位学员创建一条上课纪录
　　为学员批改成绩， 一条一条的手动修改成绩
学员视图
提交作业
查看作业成绩
一个学员可以同时属于多个班级，就像报了Linux的同时也可以报名Python一样， 所以提交作业时需先选择班级，再选择具体上课的节数
附加：学员可以查看自己的班级成绩排名


分析:

老师: 创建班级、创建课程、创建上课纪录、修改学生成绩、创建学员，查询管理班级

学员: 上传作业、查看作业成绩、查看班级排名

'''


import os
from sqlalchemy import create_engine

BASEHOME = os.path.dirname(os.path.abspath(__file__))



#create database sqlandy default character set utf8;
#grant all on sqlandy.* to 'sqlandy'@'localhost' identified by '123456';
#返回值create_engine()是一个实例 Engine
engine = create_engine('mysql+pymysql://sqlandy:123456@localhost/sqlandy')


