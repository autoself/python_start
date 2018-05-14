#!/usr/bin/env python
#-*- coding:utf8 -*-

__author__ = 'andylin'
__date__ = '18-5-10 下午2:38'

'''
create database sqlandy default character set utf8;
grant all on sqlandy.* to 'sqlandy'@'localhost' identified by '123456';
flush privileges;
'''

import os
import sys

BASEHOME = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEHOME)

from etc import setting
from sqlalchemy.orm import sessionmaker
from mode import model

model.BaseMode.metadata.create_all(setting.engine)
Session_class = sessionmaker(bind=setting.engine)
Session = Session_class()


teacher_data_01 = model.Teacher(name='alex',password='123456',relname=u'金角大王')
teacher_data_02 = model.Teacher(name='autoself',password='456123',relname=u'自由人')


grades_data_01 = model.Grades(name=u'运维主机班')
grades_data_02 = model.Grades(name=u'运维自动化班')
grades_data_03 = model.Grades(name=u'java开发脱产班')

course_data_01 = model.Course(name=u'python-Web',curriculum='90',grades_id='2')
course_data_02 = model.Course(name=u'Linux 基础',curriculum='10',grades_id='1')
course_data_03 = model.Course(name=u'基础网络',curriculum='10',grades_id='1')
course_data_04 = model.Course(name=u'java全栈开发',curriculum='180',grades_id='3')

student_data_01 = model.Student(name='lin',password='123456',relname=u'唐唐',QQ='4598772')
student_data_02 = model.Student(name='andylin',password='123456',relname=u'城城',QQ='987321')


teacher_data_01.grades = [grades_data_01,grades_data_02]
teacher_data_02.grades = [grades_data_01,grades_data_03]

student_data_01.grades = [grades_data_01,grades_data_02]
student_data_02.grades = [grades_data_01,grades_data_03]

# start_time 需要提交作业开始时间
# end_time  需要提交作业结束时间
# student_id 表示学生
# grades_id 表示班级
# course_id 表示课程
# day 表示上课节数
# status 表示状态 0 表示开启,1 表示禁止不能再提交了
record_data_01 = model.Record(start_time='2017-10-01',end_time='2017-10-07',student_id='1',grades_id='1',course_id='2',day='4',achievement='1',task='10',status='1')
record_data_02 = model.Record(start_time='2017-10-01',end_time='2017-10-07',student_id='2',grades_id='1',course_id='2',day='5',achievement='0',task='20',status='1')
record_data_03 = model.Record(start_time='2017-11-12',end_time='2017-11-27',student_id='2',grades_id='3',course_id='4',day='10',achievement='1',task='30',status='1')


Session.add_all([teacher_data_01,teacher_data_02,grades_data_01,grades_data_02,grades_data_03,\
                course_data_01,course_data_02,course_data_03,course_data_04,\
                student_data_01,student_data_02,record_data_01,record_data_02,\
                record_data_03 ])

Session.commit()

Session.close()
