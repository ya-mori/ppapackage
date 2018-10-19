import pandas as pd
from typing import Callable
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold


class CrossValidator:
    """
    Cross Validation を処理する実行機です。
    学習したモデルを返すイテレータとして振る舞います。
    """

    def k_fold(self, split: int, idx=1)->tuple:
        """
        DataFrameをn等分します。

        :param split:
        :param idx:
        :return: n等分したデータ (train, test)
        """
        fold = KFold(n_splits=split, shuffle=True, random_state=idx)
        return fold.split(self.train_data)

    def __init__(self, objective: Callable, spilt: int, train_data: pd.DataFrame, target_data: pd.DataFrame):
        """
        コンストラクタです

        :param objective: 目的関数
        :param spilt: 分割数
        :param train_data: 学習データ(DataFramePrayer)
        """
        self.objective = objective
        self.spilt = spilt
        self.train_data = train_data
        self.train_target_data = target_data
        self.k_folds = self.k_fold(spilt)
        self.index = 0

    # 新しいイテレータの作成
    def __iter__(self):
        return self

    # イテレータを進める
    def __next__(self):
        if self.index >= self.spilt - 1:
            raise StopIteration

        train_idx, valid_idx = next(self.k_folds)
        train_x, train_y = self.train_data.iloc[train_idx], self.train_target_data.iloc[train_idx]
        valid_x, valid_y = self.train_data.iloc[valid_idx], self.train_target_data.iloc[valid_idx]

        value = self.objective(train_x, train_y, valid_x, valid_y)
        index = self.index
        self.index += 1
        return index, value
