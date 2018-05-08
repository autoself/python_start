#!/usr/bin/python env 
#-*- coding:utf8 -*- 

__author__ = 'andylin'
__date__ = '18-3-5 下午9:38'


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

#channel.queue_declare(queue='hello',durable=True)

channel.exchange_declare(exchange='andylin',exchange_type='fanout')

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue


channel.queue_bind(exchange='andylin',queue=queue_name)

def callback(ch,method,properties,body):
    print('[x] Received %r ' % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)



#channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queue_name,
                      #no_ack=True
                      )
print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()