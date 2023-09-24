from kafka import KafkaProducer
import time
from json import dumps

try:
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x :dumps(x).encode('utf-8'))
except Exception as ex:
    print('Exception while connecting Kafka')
    print(str(ex))

for i in range(1000):
    producer.send("test",value={"key":i})
    print("Sending message","key",i)
    time.sleep(2)
