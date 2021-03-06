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


class BaseSchoole(object):

    def __init__(self,name,addr,city):
        self.name = name
        self.addr = addr
        self.city = city
        self.__basedir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db')
        self.__schoole_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db','schoole.db')


    def __check_english(self):
        if not os.path.isdir(self.city):
            os.makedirs(os.path.join(self.__basedir,self.city))
            return True
        else:
            return False

    def __select_db(self):
        '''
        获取最大的ID
        :return:
        '''
        if os.path.isfile(self.__schoole_db ):
            with open(self.__schoole_db ,'rb') as fs:
                db = pickle.load(fs)
            if db:
                for key in db:
                    if db[key]['name'] == self.name:
                        return True
        return False

    def create_schoole(self):
        check_nums = self.__check_english()
        if not check_nums:
            print('学校已经存在!')
            return False
        maxnums = int(self.__select_db())
        if maxnums != 0:
            with open(self.__schoole_db, 'rb') as fs:
                db = pickle.load(fs)
                print(db)
        else:
            db = {}
        maxid = maxnums + 1
        db[maxid] =  db[maxid] = {'name': self.name, 'addr': self.addr, 'city': self.city }
        with open(self.__schoole_db, 'wb') as fp:
            pickle.dump(db, fp)
        return True




class  Schoole(object):
    '''
     学校的基本信息
    '''

    def __init__(self,city):
        '''
        学校虚构函数
        :param schoole_name:           学校编号
        self.schoole_class = {}        班级
        self.schoole_course = {}       课程
        self.schoole_theacher = {}     老师
        self.schoole_student = {}      学生
        '''
        self.schoole_city = city
        self.__student_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db',self.schoole_city, 'student.db')
        self.__teacher_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db',  self.schoole_city,'teacher.db')
        self.__course_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', self.schoole_city,'course.db')
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

    def create_classe(self, name,course_name,teacher,semester):
        '''
        :param name:        班级名
        :param semester:    学期
        :param course_name: 课程
        :param teacher      讲师名
        :return:
        '''
        object_schoole = School_Class(self.__teacher_db,self.__course_db,self.__class_db,name,course_name,teacher,semester)
        db_status = object_schoole.create_class()
        if db_status:
            print('创建的班级成功%s!' % (name))
            return True
        else:
            print('创建的班级失败%s！' % (name) )
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
                        print('班级名>>%s, 课程名>>%s,讲师名>>%s,学期>>%s' % (db_class[key]['name'],db_class[key]['teacher'], db_class[key]['course_name'], db_class[key]['semester']))
                        return True

        print('对不起,没有你要查的班级')
        return False

    def create_teacher(self,name,password):
        object_db = Teacher(self.__teacher_db,name,self.schoole_city,password)
        db_stuts = object_db.create_teacher()
        if db_stuts:
            print('创建讲师成功:%s！' % (name))
            return True
        else:
            print('创建讲师失败%s！' % (name))
            return False

    def get_teacher(self,name):
        if os.path.isfile(self.__teacher_db):
            with open(self.__teacher_db, 'rb') as fs:
                db = pickle.load(fs)
            if db:
                for key in db:
                    if name == db[key]['name']:
                        print('讲师名>>%s,学区>>%s,密码>>%s' % (db[key]['name'],db[key]['schoole_city'],db[key]['password']))
                        return True

        print('对不起,没有你要查的讲师')
        return False


    def create_student(self,name,age,pay,achievement,schoole_class):
        object_db = Student(self.__student_db,self.__class_db,name,age,pay,achievement,schoole_class)
        db_status = object_db.create_student()
        if db_status :
            print('创建学生成功:%s！' % (name))
            return True
        else:
            print('创建学生失败%s！' % (name))
            return False

    def get_student(self,name):
        if os.path.isfile(self.__student_db):
            with open(self.__student_db, 'rb') as fs:
                db = pickle.load(fs)
            if db:
                for key in db:
                    if name == db[key]['name']:
                        print('学生名>>%s,年龄>>%s,缴费>>%s,成绩>>%s,班级>>%s' % (db[key]['name'], db[key]['age'], db[key]['pay'], db[key]['achievement'], db[key]['schoole_class']))
                        return True
        print('对不起,没有你要查的学生')


    def __check_student(self,db,name):
        '''
        获取班级
        :return:
        '''
        if os.path.isfile(db):
            with open(db,'rb') as fs:
                data = pickle.load(fs)
            if data:
                for key in data:
                    if data[key]['name'] == name:
                        return False
        return True
    def pull_student(self,name,pay):
        check_name = self.__check_student(self.__student_db,name)
        if check_name:
            print("\033[34;学员不存在,请先注册!\033[0m")
            return False
        with open(self.__student_db,'rb') as fs:
            data = pickle.load(fs)
        for key in data:
            if name == data[key]['name']:
                data[key]['pay'] = pay
        with open(self.__student_db,'wb') as fw:
            pickle.dump(data,fw)
        print('%s你已成功交费' % name )
        return True


    def __check_class_teacher(self,teacher_name,class_data):
        with open(self.__class_db,'rb') as fcr:
            db_class = pickle.load(fcr)
        for cdb in db_class:
            if db_class[cdb]['name'] == class_data and db_class[cdb]['teacher']:
                return True
        else:
            return False

    def get_teacher_student(self,teacher_name,class_data):
        check_class_db = self.__check_class_teacher(teacher_name,class_data)
        if not check_class_db:
            print('\033[33;1m 讲师对应的班级不存在!\033[0m')
            return False

        with open(self.__student_db,'rb') as fsr:
            st_db = pickle.load(fsr)

        check_stu = 1
        for key in st_db:
            if st_db[key]['schoole_class'] == class_data:
                check_stu = 0
                print('\033[33;1m 有学员>>>%s\033[0m' % st_db[key]['name'])
        if check_stu == 1:
            print('\033[33;1m  暂时没有任何学员！\033[0m')
        return True



    def change_teacher_course(self,teacher_name,class_data,student_name,achievement):
        check_class_db = self.__check_class_teacher(teacher_name, class_data)
        if not check_class_db:
            print('\033[33;1m 讲师对应的班级不存在!\033[0m')
            return False
        with open(self.__student_db,'rb') as fsr:
            st_db = pickle.load(fsr)

        check_stu = 1
        for key in st_db:
            if st_db[key]['schoole_class'] == class_data and st_db[key]['name'] == student_name:
                check_stu = 0
                st_db[key]['achievement'] = achievement
        if check_stu == 1:
            print('\033[33;1m  没有在讲师所在班级中找到此学员！\033[0m' )
            return False
        with open(self.__student_db,'wb') as fsw:
            pickle.dump(st_db,fsw)
        print('\033[33;1m  学员%s成绩修改完成！\033[0m' % student_name)
        return True

#if __name__ == '__main__':
#    object_schoole = Schoole('依林大学院校','北京是环市东路1号','BeiJing')
#    #object_schoole.create_course('linux','15000','30days')
#    object_schoole.get_course('linux')

