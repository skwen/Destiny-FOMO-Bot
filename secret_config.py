import configparser
import os

def read():
    """
    Read secrets/variables from a file mount, default to './config.ini'
    """
    CONFIG_PATH = os.getenv('CONFIG_PATH', 'config.ini')
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config