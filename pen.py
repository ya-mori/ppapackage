"""
Provide Python Aid Package の util モジュールです。


"""
import time
import configparser
from logger import logger as logger
import pickle


def start(file_name):
    """
    処理を実行する際のログを出力します。

    :param file_name:
    :return:
    """
    logger.info('{} start!'.format(file_name))
    global start_time
    start_time = time.time()


def end(file_name):
    """
    処理を終了する時のログを出力します。

    :param file_name:
    :return:
    """
    logger.info('{} finish!'.format(file_name))
    end_time = time.time()
    logger.info('running time: {}'.format(str(round((end_time - start_time) / 60)), 'mins'))


def read_conf():
    global config
    path = './resource/config.ini'
    config = configparser.ConfigParser().read(path)


def save_obj(object, name, path):
    """
    オブジェクトをpickleによってバイナリデータとして永続化します。

    :param object:
    :param name:
    :param path:
    :return:
    """
    with open(path + '/' + name, 'wb') as f:
        pickle.dump(object, f)


def read_obj(path):
    """
    オブジェクトをpickieによってバイナリデータから復元します。

    :param path:
    :return:
    """
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    print(obj)

