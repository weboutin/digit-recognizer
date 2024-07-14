
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import matplotlib.pyplot as plt

# 加载训练好的模型
model = load_model('model2.h5')  # 替换为您实际保存的模型文件路径

# 定义一个函数进行图片预测
def predict_digit(image_path):
    image = load_img(image_path, target_size=(28, 28))
    image = img_to_array(image)
    image = image / 255.0  # 归一化
    image = np.expand_dims(image, axis=0)  # 增加一个维度以匹配模型输入要求

    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)
    # plt.imshow(image[0])
    # plt.title(f"预测的数字: {predicted_class}")
    # plt.axis('off')
    # plt.show()
    return predicted_class

# 测试预测
for i in range(10):
    image_path = f'example2/digit_{i}.png'  # 替换为您要预测的图片路径
    predicted_digit = predict_digit(image_path)
    print(f"预测的数字: {predicted_digit}")