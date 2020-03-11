'''
占位符类型

'''
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误

input1 = tf.placeholder(tf.int32)
input2 = tf.placeholder(tf.int32)

output = tf.add(input1,input2)
session = tf.Session()
print(session.run(output,feed_dict={input1:10,input2:20}))
print(session.run(output,feed_dict={input1:40,input2:120}))
print(session.run(output,feed_dict={input1:[10,20,30],input2:[1,2,3]}))
session.close()