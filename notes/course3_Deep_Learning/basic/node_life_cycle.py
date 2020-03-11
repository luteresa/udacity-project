'''
计算图节点的依赖与生命周期

'''


import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误


k = tf.constant(222)
x = k + 12
y = x + 4
z = x * 2

with tf.Session() as session:
    print(y.eval())
    print(z.eval())

with tf.Session() as session:
    y_val,z_val = session.run([y,z])
    print(y_val)
    print(z_val)

'''
在计算图每次执行时，所有的节点都会别丢弃，但变量不会。变量是由Session维护的。除非关闭Session，否则变量会一直存在
'''