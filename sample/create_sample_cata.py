"""
サンプル用のデータを生成します。
"""

import pandas as pd
from sklearn.datasets import load_iris
from data_frame_prayer import DataFramePrayer

iris = load_iris()
train_data = pd.DataFrame(iris.data, columns=iris.feature_names)
label_data = pd.DataFrame(iris.target)

train_player = DataFramePrayer(train_data)
label_player = DataFramePrayer(label_data)

train_player.save_csv('train_data', '.')
label_player.save_csv('label_data', '.')

