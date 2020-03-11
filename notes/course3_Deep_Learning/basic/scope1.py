'''
命名作用域

'''

import tensorflow as tf

a1 = tf.Variable(10,name='a1')
a2 = tf.Variable(20,name='a2')

with tf.name_scope('param'):
    a3 = tf.Variable(30,name='a3')

with tf.name_scope('param'):  # param_1
    a4 = tf.Variable(40,name='a4')
with tf.name_scope('param'):  # param_2
    a5 = tf.Variable(40,name='a5')
for node in (a1,a2,a3,a4,a5):
    print(node.op.name)