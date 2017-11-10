#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-16 下午9:36'


import os
import pickle

class Student(object):
    '''
      学生
    '''
    def __init__(self,student_db,class_db,name,age,pay,achievement,schoole_class):
        '''
        :param city               城市
        :param name:              学生名
        :param age:               学生年龄
        :param achievement:       学生成绩
        :param schoole_class:     学生班级
        '''

        self.name = name
        self.age = age
        self.achievement = achievement
        self.pay = pay
        self.schoole_class = schoole_class
        self.__student_db =  student_db
        self.__class_db = class_db


    def __check_class(self):
        '''
        获取班级
        :return:
        '''
        if os.path.isfile(self.__class_db):
            with open(self.__class_db,'rb') as fs:
                class_db = pickle.load(fs)
            if class_db:
                for key in class_db:
                    if class_db[key]['name'] == self.schoole_class:
                        return False
        return True


    def __select_student(self):
        '''
        获取最大的ID
        :return:
        '''
        if os.path.isfile(self.__student_db):
            with open(self.__student_db,'rb') as fs:
                student_db = pickle.load(fs)
            if student_db:
                for key in student_db:
                    if student_db[key]['name'] == self.name:
                        return True
        return False


    def create_student(self):
        check_class = self.__check_class()
        if  check_class:
            print('班级不存在,请先创建班级！')
            return False
        maxnums = int(self.__select_student())
        if maxnums != 0:
            with open(self.__student_db, 'rb') as fs:
                db = pickle.load(fs)
                print(db)
        else:
            db = {}
        maxid = maxnums + 1
        db[maxid] = {'name': self.name, 'age': self.age, 'pay':self.pay,'achievement':self.achievement,'schoole_class':self.schoole_class }
        with open(self.__student_db, 'wb') as fp:
            pickle.dump(db, fp)
        return True
