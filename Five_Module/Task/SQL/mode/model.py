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
from sqlalchemy import ForeignKey,Table,Column,Integer,String,DateTime,Date
from sqlalchemy.orm import relationship,backref
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

注意在表的创建时,调用的有先后顺序性(需要研究一下)
'''


teacher_m2m_grades = Table('teacher_m2m_grades',BaseMode.metadata,
                            Column('teacher_id',Integer,ForeignKey('teacher.id')),
                            Column('grades_id',Integer,ForeignKey('grades.id')),
                            )

grades_m2m_student  = Table('grades_m2m_student',BaseMode.metadata,
                           Column('student_id',Integer,ForeignKey('student.id')),
                           Column('grades_id',Integer,ForeignKey('grades.id')),
                           )



class Grades(BaseMode):
    '''
    班级表
    '''
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    course = relationship('Course')
    #teacher = relationship('Teacher',backref='grades')
    #student = relationship('Student', backref='grades')
    record = relationship('Record')

    def __repr__(self):
        print('%s' % self.name)

class Course(BaseMode):
    '''
    课程表
    '''
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    curriculum = Column(Integer,nullable=False)
    grades_id = Column(Integer,ForeignKey('grades.id'))
    record = relationship('Record')

    def __repr__(self):
        print('%s' % self.name)


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
    grades = relationship('Grades',secondary=teacher_m2m_grades,backref='teacher')

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
    grades = relationship('Grades',secondary=grades_m2m_student, backref='student')
    record = relationship('Record')

    def __repr__(self):
        print('%s' % self.name)

class Record(BaseMode):
    '''
    上课记录表
    '''
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    start_time = Column(Date)
    end_time = Column(Date)
    achievement = Column(Integer)
    task = Column(Integer)
    status = Column(Integer)
    student_id =  Column(Integer,ForeignKey('student.id'))
    grades_id = Column(Integer,ForeignKey('grades.id'))
    course_id = Column(Integer,ForeignKey('course.id'))

    def __repr__(self):
        print('%s' % self.day)



#MetaData 是一个注册表
#BaseMode.metadata.create_all(setting.engine)
