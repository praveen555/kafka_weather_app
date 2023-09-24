import weather_api
from kafka import KafkaProducer
import time
from json import dumps
from weather_api import api_call

def run_producer():
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x :dumps(x).encode('utf-8'))
        current_time,temp,windspeed,winddirection=api_call()
        if current_time!=-1:
            data= {'current_time':current_time,'temperature':
                   temp,'windspeed':windspeed,'windirection':winddirection}
            print(data)
            producer.send("weather_app",value=data)
            #print(weather_api.current_time, weather_api.temp, weather_api.windspeed, weather_api.winddirection)
        else:
            print("API error")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))

# while True:
#     run_producer()
#     time.sleep(5)