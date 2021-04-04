import tensorflow as tf
ckpt = r'weights_SVM_partionWet/model.ckpt-10000'
import os
from tensorflow.python import pywrap_tensorflow

checkpoint_path = 'weights/model.ckpt-0'
reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path) #tf.train.NewCheckpointReader
var_to_shape_map = reader.get_variable_to_shape_map()
for key in var_to_shape_map:
	print("tensor_name: ", key)
	# print(reader.get_tensor(key))

