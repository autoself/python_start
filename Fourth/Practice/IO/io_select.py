#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'andylin'
__date__ = '18-1-14 上午10:52'



import socket
import select
import queue
import time

'''
socket.AF_INET 服务器之间网络通信
socket.SOCK_STREAM  流式socket , for TCP

s.setsockopt(level,optname,value) 设置给定套接字选项的值。


在套接字级别上(SOL_SOCKET)，option_name可以有以下取值：
SO_REUSEADDR，打开或关闭地址复用功能。
1 标记为TRUE
#操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
'''

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1',9000))
server.listen()
server.setblocking(False)

msg_dict = {}

client_input = [server,]
client_output = []

while True:
    readable , writeable, exceptional = select.select(client_input,client_output,client_input)
    #print(readable,writeable,exceptional)
    for r in readable:
        if r is server:  #别忘记,上面我们server自己也当做一个fd放在了inputs列表里,传给了select,如果这个s是server,代表server这个fd就绪了,
            #就是有活动了, 什么情况下它才有活动? 当然 是有新连接进来的时候 呀
            #新连接进来了,接受这个连接
            conn , addr = server.accept()
            print('conn: %',conn)
            client_input.append(conn) #为了不阻塞整个程序,我们不会立刻在这里开始接收客户端发来的数据, 把它放到inputs里, 下一次loop时,这个新连接
            #就会被交给select去监听,如果这个连接的客户端发来了数据 ,那这个连接的fd在server端就会变成就续的,select就会把这个连接返回,返回到
            #readable 列表里,然后你就可以loop readable列表,取出这个连接,开始接收数据了, 下面就是这么干 的

            msg_dict[conn] = queue.Queue() #接收到客户端的数据后,不立刻返回 ,暂存在队列里,以后发送

        else:
            data = r.recv(1024)
            if data:
                print(data)
                msg_dict[r].put(data)

                client_output.append(r) #放入返回的队列
            else:
                print('client close! %s' % r )
                if r in client_output:
                    client_output.remove(r)
                client_input.remove(r)
                del msg_dict[r]
            # r.send(data)
            # print("send done ....")

    for w in writeable:
        try:
            next_msg = msg_dict[w].get_nowait()
        except queue.Empty:
            print("client [%s]" % w.getpeername()[0], "queue is empty..")
            client_output.remove(w)
        else:
            print("sending msg to [%s]" % w.getpeername()[0], next_msg)
            w.send(next_msg)



    for e in exceptional:
        print("handling exception for ", e.getpeername())
        client_input.remove(e)

        if e in client_output:
            client_output.remove(e)

        e.close()

        del msg_dict[e]