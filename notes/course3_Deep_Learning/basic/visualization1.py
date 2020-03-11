'''
计算图可视化
'''
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误

x = tf.constant(20)
y = tf.constant(30)

session = tf.Session()
add = tf.add(x,y)
sub = tf.subtract(x,y)
mul = tf.multiply(x,y)
div = tf.divide(x,y)

print(session.run(add))
print(session.run(sub))
print(session.run(mul))
print(session.run(div))

# x * x + x * y + 10
xx = session.run(tf.multiply(x,x))
xy = session.run(tf.multiply(x,y))

value = tf.constant(20)
print(session.run(tf.add(session.run(tf.add(xx,xy)),value)))

result = x * x + x * y + 10
print(result)
print(session.run(result))
session.close()

# 指定常量的数据类型
str_value = tf.constant('hello tf!',dtype=tf.string)

from tensorflow_graph_in_jupyter import show_graph
print(show_graph(tf.get_default_graph()))
