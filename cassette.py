import pandas as pd


class ConversionCassette:
    """
    変換用のカセット
    DataFramePrayer にセットすることで使用できます。

    DataFrameに対する変換処理を実装する際には、ユースケース単位でこのクラスをOverrideして実装してください。
    """

    @classmethod
    def to_process(cls, dataframe):
        """
        playerで実行する処理です。
        ユースケースに合わせて適宜Overrideしてください。

        :param dataframe: データフレーム
        :return: 処理結果
        """
        return cls.add(dataframe)

    @staticmethod
    def extract(dataframe) -> pd.DataFrame:
        """
        データフレームの加工を行った結果を抽出します。

        :param dataframe: データフレーム
        :return: 抽出した結果
        """
        return dataframe

    @staticmethod
    def add(dataframe) -> pd.DataFrame:
        """
        データフレームの加工を行った結果を元のデータフレームに追加します。

        :param dataframe: データフレーム
        :return: 追加したデータフレーム
        """
        return dataframe


