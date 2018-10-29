from pathlib import Path
import pandas as pd


class DataSet:
    """
    機械学習用のデータセットを保持するクラスです。
    """

    def __init__(self, train_data: pd.DataFrame, label_data: pd.DataFrame):
        """
        コンストラクタです。

        :param train_data:
        :param label_data:
        """
        self.train_data = train_data
        self.label_data = label_data

    def is_legal(self):
        """
        データセットが正常であるか、否かを判定します。

        :return: データセットが正常であるか、否か
        """
        if len(self.train_data) != len(self.label_data):
            return False
        else:
            return True

    def count_columns(self):
        """
        データセットの列数を取得します。

        :return: (学習データのカラム数, テストデータのカラム数)
        """
        return len(self.train_data.columns), len(self.label_data.columns)

    def count_lines(self):
        """
        データセットの行数を取得します。
        :return:
        """
        return self.train_data.columns, self.label_data.columns


if __name__ == '__main__':

    current_dir = Path(__file__).resolve()

    df_train = pd.read_csv(current_dir.parent.joinpath('sample/train_data.csv'))
    df_label = pd.read_csv(current_dir.parent.joinpath('sample/train_data.csv'))

    data = DataSet(df_train, df_label)

