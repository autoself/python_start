#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-17 下午10:02'


import re
import operator







class Checknum_Class(object):

    def __init__(self,nums):
        self.nums = nums


    def Remove_parentheses(self):
        num_search = self.nums
        while True:
            check_parentheses = re.search('\([^()]+\)',num_search)
            if check_parentheses:
                op_parentheses = re.sub('[()]','',check_parentheses.group())
                self.Check_operation(op_parentheses)
                break
            else:
                break




    def Check_operation(self,opt):
        nowopt = re.sub('\s+','',opt)
        check_opt = re.findall('(\+\-|\+\+|\+|\-|\*|\/)',nowopt)
        print(check_opt)


    def Cals(self):
        pass


if __name__  == '__main__':
    #nums = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    nums = '1-2*(1+2*2/4+2*1)'

    numbers = Checknum_Class(nums)
    numbers.Remove_parentheses()