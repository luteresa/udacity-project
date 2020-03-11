'''
数据的归一化和标准化

梯度下降、k邻近
1 - 10   5            0.5

1 - 10000   5000      0.5



代价函数：最新平方误差函数

决策树、随机深林、XGBoost，都不会受特征值范围的影响

缩放数据的方法：归一化（normalization）和标准化（standardization）。

归一化：通过特征的最大最小值将特征缩放到[0,1]区间内。

标准化：通过特征的平均值和标准差将特征缩放成一个标准的正态分布，均值为0，方差为1。

sk-learn（scikit-learn）

'''

# 归一化
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = pd.read_csv('./dataset/wine.csv')
print(data.head())
minMax = MinMaxScaler()

x_normalization = minMax.fit_transform(data)

print(x_normalization)

# 标准化

from sklearn.preprocessing import StandardScaler
std = StandardScaler()

x_std = std.fit_transform(data)
print(x_std)



