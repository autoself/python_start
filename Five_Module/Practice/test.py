#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-3-5 下午8:37'


import requests
import json
import sys
import os

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=7c14830c40eccc813f7aa48fb47a67f8687af812b7985939f912ace7d2e70c4e"


def msg(text):
    json_text = {
        "msgtype": "text",
        "at": {
            "isAtAll": False
        },
        "text": {
            "content": text
        }
    }
    requests.post(api_url, json.dumps(json_text), headers=headers).content


if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)


