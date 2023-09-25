import mysql.connector
from sql_credentials import params
import time
from datetime import datetime


# Create a connection to the MySQL server
def get_connection():
    try:
        connection = mysql.connector.connect(**params)
        if connection.is_connected():
            print("Connected to MySQL database")
            cursor=connection.cursor()
            status=1


        # Perform database operations here
    except mysql.connector.Error as err:
        print("Error:", err)
        status=0
    return status,connection,cursor

def create_table_metrics():
    query=""" CREATE TABLE IF NOT EXISTS metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time DATETIME NOT NULL,
    temp FLOAT NOT NULL,
    speed FLOAT NOT NULL,
    direction FLOAT NOT NULL) """

    status,connection,cursor=get_connection()
    if status==1:
        cursor.execute(query)
        cursor.close()
        connection.close()
        print("Created Table")
    else:
        print("Error connecting SQL")


def delete_records(table_name):
    query=f"TRUNCATE TABLE {table_name}"
    status, connection, cursor = get_connection()
    if status == 1:
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
        print("Deleted records from",table_name)
    else:
        print("Error connecting SQL")

def insert_value_metrics(time, temp,speed, direction):
    data=(time, temp, speed,direction)
    query="INSERT INTO metrics (time, temp, speed, direction) VALUES (%s, %s, %s, %s)"
    status, connection, cursor = get_connection()
    if status == 1:
        cursor.execute(query,data)
        connection.commit()
        cursor.close()
        connection.close()
        print("Inserted records to metrics")
    else:
        print("Error connecting SQL")

def read_table(table_name):
    query=f"select * from metrics limit 50"
    status, connection, cursor = get_connection()
    if status == 1:
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()
        #print("Inserted records to metrics")
    else:
        print("Error connecting SQL")


# while True:
#     current_time = datetime.now()
#     current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
#     insert_value_metrics(current_time,5,10,10)
#     time.sleep(5)

#read_table("metrics")

delete_records("metrics")













