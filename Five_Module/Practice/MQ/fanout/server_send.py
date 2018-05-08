#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-3-5 下午9:38'



import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

#queue
#channel.queue_declare(queue='hello',durable=True)

channel.exchange_declare(exchange='andylin',exchange_type='fanout')

channel.basic_publish(
    exchange='andylin',
    routing_key='',
    body='hello world!',
    properties=pika.BasicProperties(
        delivery_mode=2,
    )
)

print(' [x] Sent hello world!')
connection.close()