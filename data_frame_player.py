import pandas as pd
from datetime import datetime as dt
from logger import logger as logger

from cassette import ConversionCassette
from ppap_exception import EmptyCassetteError
from ppap_exception import OverCassetteError


class DataFramePlayer:
    """
    DataFrame や ConversionCassette を差し込んで処理をする実行機です。
    """
    def __init__(self, dataframe: pd.DataFrame, cassette: ConversionCassette = None):
        """
        コンストラクタ

        :param dataframe: pandasデータフレーム
        :param cassette: 変換カセット
        """
        # DOTO データフレームの情報を出力する
        self.df = dataframe
        self.cassette = cassette

    @staticmethod
    def load_csv(path: str) -> 'DataFramePlayer':
        """
        csvデータを読み込んで DataFramePlayer を生成します

        :param path csvデータのpath
        :return: 読み込んだ DataFrame を差し込んだ Player
        """
        df = pd.read_csv(path)
        return DataFramePlayer(df)

    def save_csv(self, name: str, path: str, is_attend_date=True):
        """
        DataFrameをCSV形式で保存します。

        :param name: 保存するfile名
        :param path: 保存するpath
        :param is_attend_date: 保存する際に日付情報を付与するか、否か
        """
        if is_attend_date:
            file_name = "{0}/{1}.csv".format(path, name)
        else:
            date = dt.now().strftime('%Y%m%d%H%M')
            file_name = "{0}/{1}_{2}.csv".format(path, name, date)
        self.df.to_csv(file_name)
        logger.info("{0}を保存しました。".format(file_name))

    def add(self, cassette: ConversionCassette) -> 'DataFramePlayer':
        """
        Cassette を追加します。

        :param cassette: ConversionCassette
        :return: self
        """
        if self.cassette is not None:
            logger.warn('カセットがすでに刺さっています')  # TODO 機能していないかも
            raise OverCassetteError
        else:
            self.cassette = cassette
            return self

    def play(self) -> 'DataFramePlayer':
        """
        DataFrame に対して Cassette の処理を施します。

        :return: 加工した DataFrame
        """
        if self.cassette is None:
            logger.warn('カセットが刺さっていません')
            raise EmptyCassetteError
        else:
            self.df = self.cassette.to_process(self.df)
            return self


if __name__ == '__main__':

    player = DataFramePlayer(pd.DataFrame())
    player.add(ConversionCassette)
    player.play()
    player.add(ConversionCassette)
