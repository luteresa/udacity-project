from datetime import datetime
import tensorflow as tf
now = datetime.utcnow().strftime("%Y%m%d%H%M%S")

def relu(X):
    w_shape = (int(X.get_shape()[1]),1)
    w = tf.Variable(tf.random_normal(w_shape),name='weights')
    b = tf.Variable(0.0,name='bias')
    z = tf.add(tf.matmul(X,w),b,name='z')
    return tf.maximum(z,0,name='relu')


n_features = 3
X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")

relus = [relu(X) for i in range(5)]
output = tf.add_n(relus,name='output')

root_logdir = "tf_logs"
# 设置目录名
logdir = "{}/run-{}/".format(root_logdir, now)
file_writer = tf.summary.FileWriter(logdir, tf.get_default_graph())
file_writer.flush()
file_writer.close()