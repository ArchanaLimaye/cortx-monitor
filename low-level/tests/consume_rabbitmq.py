#!/usr/bin/env python
import pika
import socket

creds = pika.PlainCredentials('sspluser', 'sspl4ever')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', virtual_host='SSPL', credentials=creds))
channel = connection.channel()

channel.exchange_declare(exchange='sspl_bcast',
                         type='topic', durable=True)

result = channel.queue_declare(exclusive=False)
channel.queue_bind(exchange='sspl_bcast',
                   queue='SSPL-LL')

print ' [*] Waiting for json messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

channel.basic_consume(callback,
                      queue='SSPL-LL',
                      no_ack=True)

channel.start_consuming()