'''
TensorFlow中的常用运算函数

'''

import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误

x = tf.Variable(40)
y = tf.Variable(30)
k = tf.Variable(-120)
value = tf.Variable(20.5,dtype=tf.float32)
init = tf.global_variables_initializer()
with tf.Session() as session:
    init.run()
    print(session.run(tf.add(x,y)))
    print(session.run(tf.subtract(x,y)))
    print(session.run(tf.multiply(x,y)))
    print(session.run(tf.divide(x,y)))
    print(session.run(tf.mod(x,y)))  # 取余
    print(session.run(tf.abs(k)))   # 绝对值
    print(session.run(tf.negative(x)))  # 取负数
    print(session.run(tf.sign(x)),session.run(tf.sign(k))) # 返回符号， -1：负数，0：0  1：正数
    print(session.run(tf.square(x)))  # 平方
    print(session.run(tf.sqrt(value)))  # 开根号，参数值必须是float类型，否则会抛出异常
    print(session.run(tf.sin(value)))  # 正弦  参数必须是float