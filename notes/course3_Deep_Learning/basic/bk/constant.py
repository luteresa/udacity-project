'''
TensorFlow中的常量

Tensor   Flow
Tensor（张量）

TensorFlow使用Tensor来表示所有的数据。

n维数组或列表

TensorFlow

对电影进行评分


tf中的值可以由常量和变量表示




'''
import tensorflow as tf
import os

#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'  # 默认，显示所有的信息
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 只显示警告和错误
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误



hello = tf.constant('hello')
n = tf.constant(20)
print(hello)
print(n)
print(type(hello))

session = tf.Session()
print(session.run(hello))
print(str(session.run(hello),'utf-8'))

print(session.run(n))

# 指定常量的数据类型
str_value = tf.constant('hello tf!',dtype=tf.string)
print(str(session.run(str_value),'utf-8'))

#tf.constant('abc',dtype=tf.int32)

print(session.run(tf.constant(123,dtype=tf.int32)))