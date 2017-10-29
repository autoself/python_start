#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-16 下午9:18'



import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.course import Course
from src.schoole_class import   School_Class
from src.schoole_student import Student
from src.schoole_teacher import Teacher


import pickle


class  Schoole(object):
    '''
     学校的基本信息
    '''

    def __init__(self,schoole_name,schoole_addr,schoole_city):
        '''
        学校虚构函数
        :param schoole_name:           学校名称
        :param schoole_addr:           学校地址
        :param schoole_city:           学校城市
        self.schoole_class = {}        班级
        self.schoole_course = {}       课程
        self.schoole_theacher = {}     老师
        self.schoole_student = {}      学生
        '''

        self.schoole_name = schoole_name
        self.schoole_addr = schoole_addr
        self.schoole_city = schoole_city
        self.__course_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', self.schoole_city,'course.db')
        self.__student_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', self.schoole_city,'student.db')
        self.__teacher_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', self.schoole_city,'teacher.db')
        self.__class_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db',self.schoole_city,'class.db')

    def create_course(self,name,price,outline):
        '''
        创建课程
        :param name:  课程名
        :param price: 课程价格
        :param outline: 课程周期
        :return:
        '''
        object_course = Course(self.__course_db,name,price,outline)
        db_stuts = object_course.create_course()
        if db_stuts:
            print('创建课程成功:%s！' % (name))
            return True
        else:
            print('创建课程失败%s！' % (name))
            return False

    def create_schoole_classe(self, name,course_name,semester):
        '''
        :param name:        班级名
        :param semester:    学期
        :param course_name: 课程
        :return:
        '''
        object_schoole = School_Class(self.__course_db,self.__class_db,name,course_name,semester)
        db_status = object_schoole.create_class()
        if db_status:
            print('创建的班级成功%s!' % (name))
            return True
        else:
            print('创建的班级失败%s！' % (name) )
            return False


    def create_teacher(self,numbers,name,grade,school_class):
        object_teacher = Teacher(self.__teacher_db,self.__class_db,numbers,name,grade,school_class)
        db_status = object_teacher.create_teacher()
        if db_status:
            print('创建的老师成功%s!' % (name))
            return True
        else:
            print('创建的老师失败%s！' % (name) )
            return False

    def create_student(self,numbers,name,age,achievement,schoole_class):
        object_student = Student(self.__student_db,self.__class_db,numbers,name,age,achievement,schoole_class)
        db_status = object_student.create_statudent()
        if db_status:
            print('创建的学生成功%s!' % (name))
            return True
        else:
            print('创建的学生失败%s！' % (name))
            return False


    def get_course(self,name):
        if os.path.isfile(self.__course_db):
            with open(self.__course_db,'rb') as fs:
                db_course = pickle.load(fs)
            if db_course:
                for key in db_course:
                    if name == db_course[key]['name']:
                        print('课程名>>%s,课程的价格>>%s,课程的周期>>%s' %(db_course[key]['name'],db_course[key]['price'],db_course[key]['outline']))
                        return True

        print('对不起,没有你要查的课程')
        return False


    def get_class(self,name):
        if os.path.isfile(self.__class_db):
            with open(self.__class_db, 'rb') as fs:
                db_class = pickle.load(fs)
            if db_class:
                for key in db_class:
                    if name == db_class[key]['name']:
                        print('班级名>>%s, 课程名>>%s, 学期>>%s' % (db_class[key]['name'], db_class[key]['course_name'], db_class[key]['semester']))
                        return True

        print('对不起,没有你要查的班级')
        return False


    def get_teacher(self,name):
        if os.path.isfile(self.__teacher_db):
            with open(self.__teacher_db, 'rb') as fs:
                db_teacher = pickle.load(fs)
            if db_teacher:
                for key in db_teacher:
                    if name == db_teacher[key]['name']:
                        print('老师编号>>%s, 老师名>>%s, 职称>>%s,任教班级>>%s' % (db_teacher[key]['numbers'], db_teacher[key]['name'], db_teacher[key]['grade'],db_teacher[key]['schoole_class']))
                        return True
        print('对不起,没有你要查的老师')
        return False

    def get_student(self, name):
        if os.path.isfile(self.__student_db):
            with open(self.__student_db, 'rb') as fs:
                db_student = pickle.load(fs)
            if db_student :
                for key in db_student:
                    if name == db_student[key]['name']:
                        print('学号>>%s, 学生名>>%s, 年龄>>%s,成绩>>%s,班级>>%s' % (db_student[key]['numbers'], db_student[key]['name'], db_student[key]['age'],db_student[key]['achievement'], db_student[key]['schoole_class']))
                        return True
        print('对不起,没有你要查的学生')
        return False







#if __name__ == '__main__':
#    object_schoole = Schoole('依林大学院校','北京是环市东路1号','BeiJing')
#    #object_schoole.create_course('linux','15000','30days')
#    object_schoole.get_course('linux')

