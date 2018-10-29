"""
Provide Python Aid Package の util モジュールです。


"""
import time
import configparser
from logger import logger as logger
import pickle
import pathlib.Path as Path


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


def save_obj(obj: any, name: str, path: str) -> None:
    """
    オブジェクトを pickle　によってバイナリデータとして保存します。

    :param obj: 保存したいオプジェクト
    :param name: 保存名
    :param path: 保存するディレクトリの存在場所
    """
    with open(Path(path) / Path(name), 'wb') as f:
        pickle.dump(obj, f)


def read_obj(path: str) -> any:
    """
    オブジェクトを pickle によってバイナリデータから復元します。

    :param path: 復元したいバイナリデータの存在場所
    :return: 復元したオブジェクト
    """
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    return obj

