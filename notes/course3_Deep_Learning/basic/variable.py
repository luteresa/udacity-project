'''
TensorFlow中的变量

'''

import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误

x = tf.Variable(5)
y = tf.Variable(3)

f = x * x * y + y * y + 2

session = tf.Session()
session.run(x.initializer)
session.run(y.initializer)

result = session.run(f)
print(result)

# 改变变量的值
x.load(30,session)
y.load(123,session)
print(session.run(x))
result = session.run(f)
print(result)
session.close()
