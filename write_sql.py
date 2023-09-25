from consumer import run_consumer
from sql_functions import *
global buffer_size,threshold
buffer_size=[]
threshold=2
def write_to_db():
    global buffer_size
    try:
        c=run_consumer()
        print("Consumer received",c)
        buffer_size.append(c)
        print("Length of current buffer is",len(buffer_size),buffer_size)
        if len(buffer_size)> threshold:
            print("Writing to SQL Database")
            for data in buffer_size:
                t=data['current_time']
                temp=float(data['temperature'])
                wind=float(data['windspeed'])
                dir=float(data['windirection'])
                print("Values writing are",t,temp,wind,dir)
                insert_value_metrics(t,temp,wind,dir)
                buffer_size=[]
            print("the length of buffer size is",len(buffer_size))
    except Exception as e:
        print(e)
# while True:
#     write_to_db()






