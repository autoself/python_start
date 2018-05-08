#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-3-24 下午9:32'

import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1',port=6379)
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()  #打开收音机
        pub.subscribe(self.chan_sub) #调频道
        pub.parse_response()  #准备接收
        return pub