#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '17-7-23 下午3:13'


"""
 三级菜单实例化的问题
"""

areadict = {
    '广东':{
        '广州':{
            '天河':'美食城',
            '番禺':'长隆'
        },
        '深圳':{
            '福田':'政府',
            '南山':'科技园'
        }
    },
    '海南':{
        '海口':{
            '龙华':'万绿园',
            '美兰':'美食'
        },
        '三亚':{
             '吉阳':'美丽',
            '天涯':'海边'
        }
    }
}

exec_for_return = True

while exec_for_return:
    for choise1  in areadict:
        print(choise1)
    choisenow = input('输入选择省>>>')
    if choisenow in areadict:
        for choise2 in areadict[choisenow]:
            print(choise2)
        choisenow2 = input('输入选择市>>>')
        if choisenow2 in areadict[choisenow]:
            for choise3 in areadict[choisenow][choisenow2]:
                print(choise3)
            choisenow3 = input('输入选择区镇>>>')
            if choisenow3 in areadict[choisenow][choisenow2]:
                print(areadict[choisenow][choisenow2][choisenow3])
                choisenow4 = input('输入选择(q退出)>>>')
                if choisenow4 == 'q':
                    print('结束!')
                    exec_for_return = False
                else:
                    pass
        elif choisenow2 == 'q':
            print('结束!')
            exec_for_return = False
        else:
            pass
    elif choisenow == 'q':
        print('结束!')
        exec_for_return = False
    else:
        pass