import mysql.connector
from mysql.connector import Error
import configparser
import os

def load_config():
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    return config

def create_connection():
    config = load_config()
    connection = None
    try:
        connection = mysql.connector.connect(
            host=config.get('mysql', 'host'),
            user=config.get('mysql', 'user'),
            password=config.get('mysql', 'password'),
            database=config.get('mysql', 'database')
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
