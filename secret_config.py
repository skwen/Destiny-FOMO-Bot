import configparser
import os

def read():
    """
    Read secrets/variables from a file mount
    """
    CONFIG_PATH = os.getenv('CONFIG_PATH')
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config