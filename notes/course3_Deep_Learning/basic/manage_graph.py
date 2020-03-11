'''
管理计算图

'''

import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误
session = tf.Session()
x1 = tf.Variable(10,name='x1')
session.run(x1.initializer)

print(tf.get_default_graph().get_operation_by_name('x1'))
print(tf.get_default_graph().get_operation_by_name('x1').get_attr('dtype'))

print(x1.graph is tf.get_default_graph())

# 创建一个新的计算图
graph = tf.Graph()
with graph.as_default():
    x2 = tf.Variable(20)
    print(x2.graph is graph)

print(x2.graph is tf.get_default_graph())

