import json.decoder

from kafka import KafkaConsumer
import time
from json import *


def run_consumer():
    try:
        consumer = KafkaConsumer("weather_app", bootstrap_servers=['localhost:9092'],
                                     value_deserializer=lambda x: loads(x.decode('utf-8')),
                                     auto_offset_reset="latest")

        for c in consumer:
            return c.value
    except Exception as ex:
        print('Exception while connecting Kafka consumer')
        print(str(ex))

