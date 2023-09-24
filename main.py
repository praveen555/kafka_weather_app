"""
Before running start the servers with these commands in the CLI.
1.  C:/kafka/kafka_2.13-3.5.1/bin/windows/zookeeper-server-start.bat C:/kafka/kafka_2.13-3.5.1/config/zookeeper.properties

2. C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-server-start.bat C:/kafka/kafka_2.13-3.5.1/config/server.properties

3. C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-console-producer.bat --topic weather_app --bootstrap-server localhost:9092

4. C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-console-consumer.bat --topic weather_app --bootstrap-server localhost:9092
"""
import json
import time


"""
C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-topics.bat --create --topic weather_app --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
"""

from weather_api import api_call
from producer import run_producer
from consumer import run_consumer
import threading
import time

def producer_thread():
    while True:
        run_producer()
        time.sleep(5)

if __name__ == "__main__":
    while True:
        print("Running main.py")
        print("Running main.py")
        producer_thread = threading.Thread(target=producer_thread)
        producer_thread.daemon = True  # This allows the thread to exit when the main program exits
        producer_thread.start()
        # Run the consumer function in the main thread
        run_consumer()


