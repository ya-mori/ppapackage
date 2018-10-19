import pandas as pd
from datetime import datetime as dt
from logger import logger as logger
from cassette import ConversionCassette
from ppap_exception import EmptyCassetteException
from ppap_exception import OverCassetteException


class DataFramePrayer:
    """
    DataFrame や ConversionCassette を差し込んで処理をする実行機です。
    """
    def __init__(self, dataframe: pd.DataFrame, cassette: ConversionCassette = None):
        """
        コンストラクタ

        :param dataframe: pandasデータフレーム
        :param cassette: 変換カセット
        """
        self.df = dataframe
        self.cassette = cassette

    @staticmethod
    def load_csv(path: str) -> 'DataFramePrayer':
        """
        csvデータを読み込んで DataFramePlayer を生成します

        :param path csvデータのpath
        :return: 読み込んだ DataFrame を差し込んだ Player
        """
        df = pd.read_csv(path)
        return DataFramePrayer(df)

    def save_csv(self, name, path, is_attend_date=True) -> pd.DataFrame:
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

    def add_cassette(self, cassette: ConversionCassette) -> 'DataFramePrayer':
        """
        Cassette を追加します。

        :param cassette: ConversionCassette
        :return: self
        """
        if self.cassette is not None:
            logger.warn('カセットがすでに刺さっています')  #TODO 機能していないかも
            raise OverCassetteException
        else:
            self.cassette = cassette
            return self

    def play(self) -> 'DataFramePrayer':
        """
        DataFrame に対して Cassette の処理を施します。

        :return: 加工した DataFrame
        """
        if self.cassette is None:
            logger.warn('カセットが刺さっていません')
            raise EmptyCassetteException
        else:
            self.df = self.cassette.to_process(self.df)
            return self

