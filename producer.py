from json import encoder
from kafka import KafkaProducer
from kafka.serializer.abstract import Serializer
from functions import *
from time import sleep

TOPIC_NAME = '14104'

SERVER = '20.120.14.159:9092'

producer = KafkaProducer(bootstrap_servers=SERVER)

RESTRICTED = True

while(True):
    data,raw_data = produce_data()
    if RESTRICTED:
        bytestr = byteize(raw_data)
        print(data, bytestr)
        producer.send(TOPIC_NAME, bytestr.encode())
        sleep(3)
    else:
        print(data)
        producer.send(TOPIC_NAME, data)
        sleep(3)

    producer.flush()