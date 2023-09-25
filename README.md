# kafka_weather_app
## What is it ? 
Built a simple to use weather application using Kafka. The project is simple enough to execute and understand the basics of Kafka architecture and components. 


## Architecture 

![image](https://github.com/praveen555/kafka_weather_app/assets/23379996/9e7497ac-7ee5-4a1a-8655-643883d83335)

## Working

While typically your consumer, brokers and producers run on seperate machines. For this project everything is being run locally on a single machine. 

1. Currently the api data is set to 1min interval so as to not overload the free to use api service, but i have experimented on 2s,5s interval as well for a short duration
2. After receving the data from consumer we initally store in buffer size before writing to mysql. Both these parameters are users defined and can be modified freely to process batch requests.



The .csv data file is included  after running this application overnight and contains 606 records from   '2023-09-25 00:12:07' till   '2023-09-25 10:21:06'.

