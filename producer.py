from kafka import KafkaProducer
from kafka.serializer.abstract import Serializer

TOPIC_NAME = '16362'

SERVER = '20.120.14.159:9092'

producer = KafkaProducer(bootstrap_servers=SERVER)
data = b'Holis'
producer.send(TOPIC_NAME, data)

producer.flush()