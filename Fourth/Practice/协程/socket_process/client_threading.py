#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-11 下午4:38'


import socket
import threading
import time

def sock_conn():

    client = socket.socket()

    client.connect(("localhost",8001))
    count = 0
    while True:
        #msg = input(">>:").strip()
        #if len(msg) == 0:continue
        client.send( ("hello %s" %count).encode("utf-8"))

        data = client.recv(1024)

        print("[%s]recv from server:" % threading.get_ident(),data.decode()) #结果
        count +=1
        time.sleep(2)
    client.close()



t_list=[]
for i in range(2):
    t = threading.Thread(target=sock_conn)
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()
