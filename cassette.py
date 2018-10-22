import pandas as pd

from ppap_exception import CassetteValidateException


class CassetteValidator:
    """
    カセットが取り扱うデータのパリデーションチェックを行います。
    """

    @classmethod
    def run(cls, dataframe):
        if type(dataframe) is pd.DataFrame:
            raise CassetteValidateException


class ConversionCassette:
    """
    変換用のカセット
    DataFramePrayer にセットすることで使用できます。

    DataFrameに対する変換処理を実装する際には、ユースケース単位でこのクラスをOverrideして実装してください。
    """

    validation = CassetteValidator()

    @staticmethod
    def to_process(dataframe):
        """
        playerで実行する処理です。
        ユースケースに合わせて適宜Overrideしてください。

        :param dataframe: データフレーム
        :return: 処理結果
        """
        ConversionCassette.validation.run(dataframe)
        return dataframe

    @staticmethod
    def extract(dataframe) -> pd.DataFrame:
        """
        データフレームの加工を行った結果を抽出します。

        :param dataframe: データフレーム
        :return: 抽出した結果
        """
        ConversionCassette.validation.run(dataframe)
        return dataframe

    @staticmethod
    def add(dataframe) -> pd.DataFrame:
        """
        データフレームの加工を行った結果を元のデータフレームに追加します。

        :param dataframe: データフレーム
        :return: 追加したデータフレーム
        """
        ConversionCassette.validation.run(dataframe)
        return dataframe

