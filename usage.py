
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



from tensorflow.keras.models import load_model

model = load_model('model.h5')  # 加载保存的模型


# 读取新图片

for i in range(10):
    image_path = f'example/digit_{i}.png'  # 替换为您的图片路径
    image = Image.open(image_path).convert('L')  # 转换为灰度图
    image = image.resize((28, 28))  # 调整大小为 28x28
    image_array = np.array(image)  # 转换为 numpy 数组

    # 数据预处理
    image_array = image_array.reshape(1, 28, 28, 1) / 255.0  # 增加维度并归一化


    # # 进行预测
    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction)  # 获取预测的类别

    # # 显示结果
    print(f'预测的数字为: {predicted_class}')
    plt.imshow(image_array.reshape(28, 28), cmap='gray')  # 显示输入的图片
    plt.title(f'预测: {predicted_class}')
    plt.show()
