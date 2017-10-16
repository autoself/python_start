#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-10-16 下午9:18'



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
        self.schoole_classrecord = {}  课程表
        self.schoole_gradechart = {}   上课记录 与 成绩

        '''

        self.schoole_name = schoole_name
        self.schoole_addr = schoole_addr
        self.schoole_city = schoole_city
        self.schoole_class = {}
        self.schoole_course = {}
        self.schoole_theacher = {}
        self.schoole_student = {}
        self.schoole_classrecord = {}
        self.schoole_gradechart = {}



    def create_schoole_classe(self):
        pass

    