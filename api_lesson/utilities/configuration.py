import configparser
import mysql.connector
from mysql.connector import Error
import os
from dotenv import find_dotenv, load_dotenv


def getConfig():
    load_dotenv(find_dotenv())
    config = configparser.ConfigParser()
    config.read(os.getenv("PROPERTIES_DIR"))
    return config


def getPassword():
    load_dotenv(find_dotenv())
    password = os.getenv('GIT_PASS')
    return password


connect_config = {
    "user": getConfig()['SQL']['user'],
    "password": getConfig()['SQL']['password'],
    "host": getConfig()['SQL']['host'],
    "database": getConfig()['SQL']['database']
}


def getDBConnection():
    try:
        conn = mysql.connector.connect(**connect_config)  # ** is used to specify that a dictionary is used
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getDBConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
