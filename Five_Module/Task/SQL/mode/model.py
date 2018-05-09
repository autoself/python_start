#!/usr/bin/env python
#-*- coding:utf8 -*-

__author__ = 'andylin'
__date__ = '18-5-9 上午11:40'



import os
import sys

BASEHOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEHOME)

from etc import setting

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime

#声明基类
BaseMode = declarative_base()

'''
create_time = db.Column(DateTime, default=datetime.now)
create_time = db.Column(DateTime, default=datetime.now())
两者的区别:
第一个插入的起期望的, 数据的插入时间
第二条是一个固定的时间, 程序部署的时间

如果想想在生成的table中有默认值使用server_default
'''

class Teacher(BaseMode):
    '''
    老师的表
    '''
    __tablename__ = 'teacher'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    password = Column(String(64),nullable=False)
    relname = Column(String(32))
    create_time = Column(DateTime,default=datetime.now)
    login_time = Column(DateTime,nullable=True)

    def __repr__(self):
        print('%s' % self.name)


class Student(BaseMode):
    '''
    学员的表
    '''
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    password = Column(String(64), nullable=False)
    relname = Column(String(32))
    QQ = Column(Integer,nullable=False)
    create_time = Column(DateTime, default=datetime.now)
    login_time = Column(DateTime, nullable=True)


class Course(BaseMode):
    '''
    课程表
    '''
    ___tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)


class Grades(BaseMode):
    '''
    班级表
    '''
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)


class Record(BaseMode):
    '''
    上课记录表
    '''
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    num = Column(Integer)



#MetaData 是一个注册表
BaseMode.metadata.create_all(setting.engine)
