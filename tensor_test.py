import tensorflow as tf
import numpy as np

a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
b = tf.zeros_like(a)
c=tf.ones([16,2],tf.float32)
c=c*2-1

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(a))
print(sess.run(b))
print(sess.run(c))