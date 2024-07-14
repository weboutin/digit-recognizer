from PIL import Image

# 定义数字模板的特征
digit_templates = {
    0: {'area': 1000, 'perimeter': 400},
    1: {'area': 200, 'perimeter': 100},
    2: {'area': 800, 'perimeter': 300},
    3: {'area': 600, 'perimeter': 250},
    4: {'area': 700, 'perimeter': 280},
    5: {'area': 500, 'perimeter': 220},
    6: {'area': 900, 'perimeter': 350},
    7: {'area': 300, 'perimeter': 150},
    8: {'area': 1100, 'perimeter': 420},
    9: {'area': 400, 'perimeter': 180}
}
def preprocess_image(image_path):
    """
    图像预处理，灰度化和二值化
    """
    image = Image.open(image_path).convert('L')
    threshold = 128
    image = image.point(lambda p: p > threshold and 255)
    image.save('a.png')
    return image

# def preprocess_image(image_path):
#     """
#     图像预处理，灰度化和二值化
#     """
#     # 打开图片
#     img = Image.open(image_path)

#     # 灰度化
#     gray_img = img.convert('L')

#     # 二值化，阈值设为 128，可根据实际情况调整
#     threshold = 128
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#     binary_img = gray_img.point(table, '1')

#     # 保存二值化后的图片
#     binary_img.save("test.png")
#     return binary_img

def extract_features(image):
    """
    提取图像特征，这里简单计算面积和周长
    """
    pixels = image.load()
    width, height = image.size
    area = 0
    perimeter = 0

    for x in range(width):
        for y in range(height):
            if pixels[x, y] == 255:
                area += 1
                if x > 0 and pixels[x - 1, y] == 0 or y > 0 and pixels[x, y - 1] == 0:
                    perimeter += 1

    return {'area': area, 'perimeter': perimeter}

def match_template(features):
    """
    与数字模板进行特征匹配
    """
    min_diff = float('inf')
    recognized_digit = -1

    for digit, template_features in digit_templates.items():
        area_diff = abs(features['area'] - template_features['area'])
        perimeter_diff = abs(features['perimeter'] - template_features['perimeter'])
        total_diff = area_diff + perimeter_diff

        if total_diff < min_diff:
            min_diff = total_diff
            recognized_digit = digit

    return recognized_digit

# 测试
for i in range(10):
    image_path = f'./digit_{i}.png'  # 替换为您的图片路径
    processed_image = preprocess_image(image_path)

    features = extract_features(processed_image)
    recognized_digit = match_template(features)
    print("识别到的数字:", recognized_digit)

# 打开图片
# img = Image.open(image_path)

# # 转换为灰度图
# gray_img = img.convert('L')

# # 自定义阈值，这里设置为 128，可根据需要调整
# threshold = 128
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)

# # 应用二值化
# binary_img = gray_img.point(table, '1')

# # 显示二值化后的图片
# binary_img.show()

# try:
#     image = Image.open(image_path)
#     image.show() 
# except Exception as e:
#     print("发生错误:", e)
