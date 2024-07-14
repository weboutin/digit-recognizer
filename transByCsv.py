import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# 读取 CSV 文件
data = pd.read_csv('data.csv')

# 提取图片路径和标签
image_paths = data['image_path']
labels = data['label']

def process_image(image_path):
    image = load_img(image_path, target_size=(28, 28))  # 假设图片需要调整为 28x28
    image = img_to_array(image)
    image = image / 255.0  # 归一化
    return image

# 处理图片并转换为数组
X = np.array([process_image(path) for path in image_paths])
y = np.array(labels)

# 对标签进行独热编码
y = tf.keras.utils.to_categorical(y, num_classes=10)  # 假设数字类别为 0 到 9

# 构建模型
model = Sequential([
    Flatten(input_shape=(28, 28, 3)),  # 假设图片是彩色的，通道数为 3
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
model.fit(X, y, epochs=10, batch_size=32, validation_split=0.1)

model.save('model2.h5')
# 在测试集上评估模型（如果有）
# test_loss, test_acc = model.evaluate(X_test, y_test)
# print(f"Test Loss: {test_loss}, Test Accuracy: {test_acc}")