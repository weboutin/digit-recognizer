
# import tensorflow as tf
# if tf.config.list_physical_devices('GPU'):
#     print("GPU is available")
# else:
#     print("GPU is not available")


# from tensorflow.python.client import device_lib

# print(device_lib.list_local_devices())

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
import gzip

def load_mnist_local(path):
    with gzip.open(path + 'train-images-idx3-ubyte.gz', 'rb') as f:
        train_images = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1, 28, 28)
    with gzip.open(path + 'train-labels-idx1-ubyte.gz', 'rb') as f:
        train_labels = np.frombuffer(f.read(), np.uint8, offset=8)
    with gzip.open(path + 't10k-images-idx3-ubyte.gz', 'rb') as f:
        test_images = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1, 28, 28)
    with gzip.open(path + 't10k-labels-idx1-ubyte.gz', 'rb') as f:
        test_labels = np.frombuffer(f.read(), np.uint8, offset=8)
    return (train_images, train_labels), (test_images, test_labels)

# 假设数据集文件存放在当前目录的'mnist_data'文件夹下
local_path ='mnist_data/'
(x_train, y_train), (x_test, y_test) = load_mnist_local(local_path)
# (train_images, train_labels), (test_images, test_labels) = load_mnist_local(local_path)

# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# 数据预处理
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1) / 255.0
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)

# # 构建模型
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# # 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# # 训练模型
model.fit(x_train, y_train, epochs=10, batch_size=128, validation_split=0.1)

# # 评估模型
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

model.save('model.h5')