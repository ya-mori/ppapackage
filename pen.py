"""
Provide Python Aid Package の util モジュールです。


"""
import time
import configparser
from logger import logger as logger


def start():
    global start_time
    start_time = time.time()


def end():
    end_time = time.time()
    logger.info('running time: {}'.format(str(round((end_time - start_time) / 60)), 'mins'))


def read_conf():
    global config
    path = './resource/config.ini'
    config = configparser.ConfigParser().read(path)



