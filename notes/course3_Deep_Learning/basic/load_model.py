import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 只显示错误
theta = tf.Variable(tf.random_uniform([9,1],-1.0,1.0,seed=45))  # 初始化theta
saver = tf.train.Saver()

with tf.Session() as session:
    saver.restore(session,'./models/gradients.ckpt')
    best_theta_restored = theta.eval()
print(best_theta_restored)
