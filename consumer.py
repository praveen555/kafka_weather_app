from kafka import KafkaConsumer
import time
from json import *
try:
    consumer = KafkaConsumer("test",bootstrap_servers=['localhost:9092'],value_deserializer=lambda x :loads(x.decode('utf-8')),auto_offset_reset="earliest")
except Exception as ex:
    print('Exception while connecting Kafka')
    print(str(ex))

while True:
    for c in consumer:
        print(c.value)