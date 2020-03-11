'''
用TensorFlow实现线性回归算法

线性：一条直线

回归：拟合出一条直线

线性回归：主要进行预测

预测：分析已经有的数据，然后找到这些数据的规律，最后根据这些规律计算未知的数据

sk-learn
'''

import tensorflow as tf
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
m,n = housing.data.shape
print('m:',m,'n:',n)
# 变成了20640行，9列   第1列都是1（添加了X0）
housing_data_plus_bias = np.c_[np.ones((m,1)),housing.data]
print(housing_data_plus_bias)

print(housing.target)
print(housing.target.reshape(-1,1))

# 构建计算图
X = tf.constant(housing_data_plus_bias,dtype=tf.float32,name='X')
y = tf.constant(housing.target.reshape(-1,1),dtype=tf.float32,name='y')

# 计算矩阵的转置
XT = tf.transpose(X)
theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT,X)),XT),y)

with tf.Session() as session:
    theta_value = theta.eval()
    print(theta_value)

print(housing_data_plus_bias[0])

values = np.array([1.,8.3252,41.,6.98412698,1.02380952,322.,2.55555556, 37.88,-122.23]).reshape(1,9)
Values = tf.constant(values,dtype=tf.float32,name='values')
with tf.Session() as session:
    predict = tf.matmul(Values,theta_value).eval()
    print(predict[0][0])  # 4.131298

print(housing.target[0]) # 4.526
