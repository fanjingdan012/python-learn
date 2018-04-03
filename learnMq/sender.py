#!/usr/bin/env python
import pika
credentials = pika.PlainCredentials('root', 'Initial0')
parameters = pika.ConnectionParameters('localhost',
                                       5673,
                                       '/',
                                       credentials)
# connection = pika.BlockingConnection(pika.ConnectionParameters(
#     host='localhost'))
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
# channel.exchange_declare(exchange='logs',
#                          type='fanout')
channel.basic_publish(exchange='SharedExchange',
                      routing_key='SocialMessage.CREATE.94802546213728',
                      body='{"version":11,"customFields":{},"id":379840165257216,"platform":"INSTAGRAM","account":"3034613191","displayName":"leimiaomiaomiao","imageUrl":"https://scontent.cdninstagram.com/t51.2885-19/s150x150/12424649_1588024974853159_324456840_a.jpg","homepageUrl":"https://www.instagram.com/leimiaomiaomiao"}',
                      properties=pika.BasicProperties(
                          delivery_mode=2,headers={'X-Tenant-ID': '94802546213728','X-User-Type': 'key','X-Business-Key': '379840165257216','X-Session-ID': '','X-User-ID': '379210401800192','X-Event-Time': '1513763457552','X-Employee-ID': '379210415194208','X-Access-Token': '','X-Trace-ID': '2a767b00-649d-432a-a02c-b0113e441737','X-Event-Type': 'SocialMessage/UPDATE','X-System-Locale': 'en_US','apiVersion': 'com.sap.sme.anw.api.v1.campaign.resource.SocialMessage','X-Ro-ID': '379840165257216','X-Locale': 'en_US','X-B3-SpanId': '64383703d8382989','X-Action-Type': 'UPDATE','X-Message-ID': '0a4ce525-33d7-442e-84c2-0cff84dcd3c4','X-B3-TraceId': '64383703d8382989','X-Object-Version': '11','X-Object-Name': 'SocialMessage'}
                          # 标记我们的消息为持久化的 - 通过设置 delivery_mode 属性为 2
                          # 这样必须设置，让消息实现持久化
                      ))


# channel.queue_declare(queue='hello')
#
# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()