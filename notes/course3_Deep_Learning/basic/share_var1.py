from datetime import datetime
import tensorflow as tf
now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
n_features = 3

with tf.variable_scope("relu"):
    threshold = tf.get_variable("threshold", shape=(),
                                initializer=tf.constant_initializer(0.0))
# 如果变量不存在，get_variable函数会创建一个新的变量
# 去掉reuse（默认是False），会抛出异常，默认为了防止因为误操作多次获取变量，如果要共享，可以设为True
with tf.variable_scope("relu", reuse=True):
   threshold = tf.get_variable("threshold", initializer=tf.constant_initializer(0.0))
with tf.variable_scope("relu") as scope:
    scope.reuse_variables()
    threshold = tf.get_variable("threshold")

def relu(X):
    with tf.variable_scope("relu", reuse=True):
        threshold = tf.get_variable("threshold")
        w_shape = int(X.get_shape()[1]), 1                          # not shown
        w = tf.Variable(tf.random_normal(w_shape), name="weights")  # not shown
        b = tf.Variable(0.0, name="bias")                           # not shown
        z = tf.add(tf.matmul(X, w), b, name="z")                    # not shown
        return tf.maximum(z, threshold, name="max")

X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")

relus = [relu(X) for relu_index in range(5)]
output = tf.add_n(relus, name="output")

file_writer = tf.summary.FileWriter("logs/relu6", tf.get_default_graph())
file_writer.close()