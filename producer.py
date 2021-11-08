from kafka import KafkaProducer
from kafka.serializer.abstract import Serializer
from functions import *
from time import sleep

TOPIC_NAME = '16362'

SERVER = '20.120.14.159:9092'

producer = KafkaProducer(bootstrap_servers=SERVER)

while(True):
    data = produce_data()
    print(data)
    sleep(3)
    producer.send(TOPIC_NAME, data)

    producer.flush()