"""
LightGBMを用いた判別処理をまとめたモジュール群です。
"""


import pandas as pd
from lightgbm import LGBMClassifier


def run_lightgbm(model: LGBMClassifier, train_x: pd.DataFrame, train_y: pd.DataFrame, eval_set: tuple) -> LGBMClassifier:
    """
    LightGBMを使った分類を行います

    param
        model: LightGBMModel
        train_x: train data
        train_y: train label data
        eval_set: 検証用の data set -tupleのlist
        verbose:
    return
        clf.fit()の実行結果
    """
    clf = model
    clf.fit(train_x,
            train_y,
            eval_set=eval_set,
            eval_metric='auc',
            verbose=True,
            early_stopping_rounds=300)
    return clf


def analyze_lightgbm(clf: LGBMClassifier, feature_columns: pd.Series) -> pd.DataFrame:
    """
    LightGBMを使った分類結果を評価します。

    :param clf: 分類機
    :param feature_columns: 特徴量のカラム
    :return: 評価データ
    """
    importance_df = pd.DataFrame()
    importance_df["feature"] = feature_columns
    importance_df["importance"] = clf.feature_importances_
    return importance_df
