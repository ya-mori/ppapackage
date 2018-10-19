"""
ppapackage の使用例を実装したサンプルコードです。

"""

import pandas as pd
from lightgbm import LGBMClassifier

import pen
import lightgbm_executer as lgbexe
from logger import logger as logger
from cross_validator import CrossValidator
from cassette import ConversionCassette
from data_frame_prayer import DataFramePrayer


"""
ケースにあわせて定義するもの

・それぞれのユースケースに合わせてデータを処理するカセット
・機械学習のモデルを使った処理
"""


class MeanCassette(ConversionCassette):
    """
    平均値を計算するカセットです。
    """
    @staticmethod
    def to_process(dataframe: pd.DataFrame) -> pd.Series:
        return MeanCassette.extract(dataframe)

    @staticmethod
    def extract(dataframe: pd.DataFrame) -> pd.Series:
        return dataframe.mean


class CleanLabelCassette(ConversionCassette):
    """
    ラベル用のデータを整形するカセットです。
    """
    @staticmethod
    def to_process(dataframe: pd.DataFrame) -> pd.Series:
        super().to_process(dataframe)
        return CleanLabelCassette.extract(dataframe)

    @staticmethod
    def extract(dataframe: pd.DataFrame) -> pd.Series:
        super().extract(dataframe)
        return dataframe['0']


def __objective(train, train_target, valid, valid_target):
    """
    モデルの設定をして学習を行います。
    返り値は学習したモデルである必要があります。

    :param train: 学習用訓練データ
    :param train_target: 学習用解答データ
    :param valid: 評価用訓練ダータ
    :param valid_target: 評価用解答データ
    :return: 学習済みのモデル
    """
    # 適当に設定する
    model = LGBMClassifier(
        boosting_type='dart',
        random_state=1,
        n_estimators=10000,
        num_leaves=32,
        learning_rate=0.015209629834941068,
        colsample_bytree=0.18425638982476444,
        subsample=0.7744220618085227,
        subsample_freq=1,
        lambda_l1=0.08034075341606496,
        lambda_l2=0.013006632140392122,
        min_split_gain=0.023391277578902834,
        min_child_weight=40
    )

    eval_set = [(valid, valid_target)]

    return lgbexe.run_lightgbm(
        model=model,
        train_x=train,
        train_y=train_target,
        eval_set=eval_set
    )


"""
Main処理
"""
if __name__ == '__main__':

    logger.info('example start!')

    pen.start()

    train_data_path = './sample/train_data.csv'
    label_data_path = './sample/label_data.csv'

    # データの読み込み
    train_data_player = DataFramePrayer.load_csv(train_data_path)
    label_data_player = DataFramePrayer.load_csv(label_data_path)

    # 平均値の算出
    train_data_mean = MeanCassette.extract(train_data_player.df)

    label_data_player.add_cassette(CleanLabelCassette).play()

    spilt = 5

    # クロスバリデーションの設定
    validator = CrossValidator(
        objective=__objective,
        spilt=spilt,
        train_data=train_data_player.df,
        label_data=label_data_player.df
    )

    feature_columns = train_data_player.df.columns

    sub_predicts = pd.DataFrame()
    for folds, clf in validator:
        predicts = clf.predict_proba(train_data_player.df, num_iteration=clf.best_iteration_)[:, 1] / spilt
        fold_importance_df = lgbexe.analyze_lightgbm(clf, feature_columns)

    DataFramePrayer(sub_predicts).save_csv('result', './', is_attend_date=True)

    pen.end()

