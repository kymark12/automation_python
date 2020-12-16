import configparser
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
