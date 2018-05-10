#!/usr/bin/env python
#-*- coding:utf8 -*-

__author__ = 'andylin'
__date__ = '18-5-10 下午2:38'


import os
import sys

BASEHOME = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEHOME)

from etc import setting
from sqlalchemy.orm import sessionmaker
from mode import model


Session_class = sessionmaker(bind=setting.engine)
Session = Session_class()


teacher_data_01 = model.Teacher(name='alex',password='123456',relname=u'金角大王')
teacher_data_02 = model.Teacher(name='autoself',password='456123',relname=u'自由人')


grades_data_01 = model.Grades(name=u'运维主机班')
grades_data_02 = model.Grades(name=u'运维自动化班')
grades_data_03 = model.Grades(name=u'java开发脱产班')

course_data_01 = model.Course(name=u'python-Web',curriculum='90',grades_id='2')
course_data_01 = model.Course(name=u'Linux 基础',curriculum='10',grades_id='1')
course_data_02 = model.Course(name=u'java全栈开发',curriculum='180',grades_id='3')

student_data_01 = model.Student(name='lin',password='123456',relname=u'唐唐',QQ='4598772')
student_data_02 = model.Student(name='andylin',password='123456',relname=u'城城',QQ='987321')



