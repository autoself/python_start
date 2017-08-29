#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-8-17 下午10:02'

import re



import  re

def common_sub(args):
    '''
    计算结果
    :param args:
    :return:
    '''
    while True:
        if args.__contains__('+-') or args.__contains__('--') or args.__contains__('++') or args.__contains__('-+'):
            args = args.replace('+-', '-')
            args = args.replace('++', '+')
            args = args.replace('-+', '-')
            args = args.replace('--', '+')
        else:
            break
    check_status = re.search('[\+\-]?\d+\.?\d*[\*\/]{1}[\+\-]?\d+\.?\d*',args)
    if not check_status:
        return args
    str_sub = check_status.group()
    check_strs = list(str_sub.rpartition('*'))
    check_len = [i for i in check_strs if i != '']
    if len(check_len) != 3:
        check_strs = list(str_sub.rpartition('/'))
    if check_strs[1] == '*':
        value = float(check_strs[0]) * float(check_strs[2])
    else:
        value = float(check_strs[0]) / float(check_strs[2])
    #after = re.split('[\+\-]?\d+\.?\d*[\*\/]{1}[\+\-]?\d+\.?\d*', args, 1)
    if value > 0:
        value = '+%s' % (str(value))
    args = args.replace(str_sub, str(value))
    return common_sub(args)


def common_add_sub(args):
    '''
    计算加减
    :param args:
    :return:
    '''
    while True:
        if args.__contains__('+-') or args.__contains__('--') or args.__contains__('++') or args.__contains__('-+'):
            args = args.replace('+-', '-')
            args = args.replace('++', '+')
            args = args.replace('-+', '-')
            args = args.replace('--', '+')
        else:
            break
    check_status = re.search('[\+\-]?\d+\.?\d*[\+|\-]{1}\d+\.?\d*',args)
    if not check_status:
        return  args
    str_sub = check_status.group()
    check_strs = list(str_sub.rpartition('-'))
    check_len = [ i for i in check_strs if i !='' ]
    if len(check_len) != 3:
        check_strs = list(str_sub.rpartition('+'))
    if  check_strs[1] == '+' :
        value = float(check_strs[0])+float(check_strs[2])
    else:
        value = float(check_strs[0])-float(check_strs[2])
    #after  = re.split('[\+\-]?\d+\.?\d*[\+|\-]{1}\d+\.?\d*',args,1)
    args = args.replace(str_sub,str(value))
    return common_add_sub(args)



def common_all_div(arg):
    '''
    计算加减乘除
    :param arg:
    :return:
    '''

    #乘除
    arg = common_sub(arg)

    #计算加减
    arg = common_add_sub(arg)

    return arg



def main_info(numbers):
    inapp = re.search('\(([\+\-\*\/]*\d+\.?\d*){2,}\)',numbers)
    if not inapp:
        args = common_all_div(numbers)
        return args

    str_sub = inapp.group()
    ret = str_sub[1:len(str_sub)-1]
    args = common_all_div(ret)
    numbers = numbers.replace(str_sub,args)
    return main_info(numbers)



if __name__ == '__main__':

    input_num ="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    #input_num = "1-2*-30/-12*(-20+200*-3/-200*-300-100)"
    #input_num = "1-2-(3.3/5-12*20)"
    innum = re.sub('\s+','',input_num)
    args = main_info(innum)
    print('The end result >>>',args)
