'''
初始化TensorFlow变量的方法

'''

import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误


x = tf.Variable(5)
y = tf.Variable(3)

f = x * x * y + y * y + 2

with tf.Session() as session:
    x.initializer.run()
    y.initializer.run()
    result = f.eval()
print(result)


'''
并不会一下子初始化，而是在计算图中创建一个节点，这个节点会在会话执行时初始化所有的变量

惰性初始化
'''

init = tf.global_variables_initializer()

with tf.Session() as session:
    init.run()
    result = f.eval()
print(result)

'''
一个TensorFlow程序分为两部分：
1. 用于构建计算图的部分
2. 用于执行计算图的部分
'''