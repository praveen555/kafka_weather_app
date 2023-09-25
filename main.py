"""
do not forget to deactivate from the venv when you running this from the IDE terminal.
Before running start the servers with these commands in the CLI.
1.  C:/kafka/kafka_2.13-3.5.1/bin/windows/zookeeper-server-start.bat C:/kafka/kafka_2.13-3.5.1/config/zookeeper.properties

2. C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-server-start.bat C:/kafka/kafka_2.13-3.5.1/config/server.properties

3. C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-console-producer.bat --topic weather_app --bootstrap-server localhost:9092

4. C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-console-consumer.bat --topic weather_app --bootstrap-server localhost:9092
"""


"""
C:/kafka/kafka_2.13-3.5.1/bin/windows/kafka-topics.bat --create --topic weather_app --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
"""

from producer import run_producer
from write_sql import write_to_db,buffer_size,threshold
import threading
import time
buffer_size=[]
def producer_thread():
    while True:
        run_producer()
        time.sleep(60)

if __name__ == "__main__":
    print("Running main.py")
    producer_thread_instance = threading.Thread(target=producer_thread)
    producer_thread_instance.daemon = True  # This allows the thread to exit when the main program exits
    producer_thread_instance.start()
    while True: # Run the consumer function in the main thread
        write_to_db()


