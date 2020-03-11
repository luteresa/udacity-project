'''
用TensorFlow实现梯度下降算法


梯度下降算法：一点一点尝试

通过迭代的方式不断调整参数，从而让成本函数最小化

曲线某一点的导数的几何意义就是改点在曲线上的斜率（与改点的切线有关）

求曲线的最小值，也就是求导数等于0的点

求成本函数的最小值

学习率：太低，步长太小，需要非常长的时间才能迭代完


'''

import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误

import numpy as np

n_epochs = 1000  # 迭代次数
learning_rate = 0.01 # 学习率
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
m,n = housing.data.shape
print('m:',m,'n:',n)

# 标准化
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_housing_data = scaler.fit_transform(housing.data)
scaled_housing_data_plus_bias = np.c_[np.ones((m,1)),scaled_housing_data]
print(scaled_housing_data_plus_bias)

# 建立计算图
X = tf.constant(scaled_housing_data_plus_bias,dtype=tf.float32,name='X')
y = tf.constant(housing.target.reshape(-1,1),dtype=tf.float32,name='y')

theta = tf.Variable(tf.random_uniform([n+1,1],-1.0,1.0,seed=45))  # 初始化theta

init = tf.global_variables_initializer()
with tf.Session() as session:
    session.run(init)
    print(theta.eval())

y_pred = tf.matmul(X,theta,name='predictions')  # 矩阵相乘，得到y
error = y_pred - y # 误差
mse = tf.reduce_mean(tf.square(error),name='mse')  # 计算mse（均方误差）成本函数
gradients = tf.gradients(mse,[theta])[0]
# 创建一个变量赋值的节点，将第2个参数值赋给第1个参数
training_op = tf.assign(theta,theta-learning_rate * gradients)

init = tf.global_variables_initializer()
saver = tf.train.Saver()
with tf.Session() as session:
    session.run(init)
    # 开始迭代1000次
    for epoch in range(n_epochs):
        if epoch % 100 == 0:
            print('Epoch',epoch,'mse=',mse.eval())
        session.run(training_op)
    best_theta = theta.eval()
    save_path = saver.save(session,'./models/gradients.ckpt')
    print(save_path)
print('best theta:',best_theta)
