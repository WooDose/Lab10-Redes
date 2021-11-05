from kafka import KafkaConsumer

TOPIC_NAME = '16362'

SERVER = '20.120.14.159:9092'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=SERVER)

for message in consumer:
    print(message)