


from PIL import Image

# 定义数字模板的特征
digit_templates = {
    0: {
        'area': 1000, 
        'perimeter': 400, 
        'width_height_ratio': 1.0,  # 宽高比
        'top_bottom_symmetry': True,  # 上下对称性
        'left_right_symmetry': True  # 左右对称性
    },
    1: {
        'area': 200, 
        'perimeter': 100, 
        'width_height_ratio': 0.1,
        'top_bottom_symmetry': False,
        'left_right_symmetry': False
    },
    2: {
        'area': 800, 
        'perimeter': 300, 
        'width_height_ratio': 0.5,
        'top_bottom_symmetry': False,
        'left_right_symmetry': False
    },
    3: {
        'area': 600, 
        'perimeter': 250, 
        'width_height_ratio': 0.5,
        'top_bottom_symmetry': False,
        'left_right_symmetry': False
    },
    4: {
        'area': 700, 
        'perimeter': 280, 
        'width_height_ratio': 0.2,
        'top_bottom_symmetry': False,
        'left_right_symmetry': False
    },
    5: {
        'area': 500, 
        'perimeter': 220, 
        'width_height_ratio': 0.5,
        'top_bottom_symmetry': False,
        'left_right_symmetry': False
    },
    6: {
        'area': 900, 
        'perimeter': 350, 
        'width_height_ratio': 0.5,
        'top_bottom_symmetry': True,
        'left_right_symmetry': False
    },
    7: {
        'area': 300, 
        'perimeter': 150, 
        'width_height_ratio': 0.1,
        'top_bottom_symmetry': False,
        'left_right_symmetry': False
    },
    8: {
        'area': 1100, 
        'perimeter': 420, 
        'width_height_ratio': 1.0,
        'top_bottom_symmetry': True,
        'left_right_symmetry': True
    },
    9: {
        'area': 400, 
        'perimeter': 180, 
        'width_height_ratio': 0.5,
        'top_bottom_symmetry': False,
        'left_right_symmetry': False
    }
}

def preprocess_image(image_path):
    """
    图像预处理，包括灰度化、二值化和边界提取
    """
    image = Image.open(image_path).convert('L')
    threshold = 128
    image = image.point(lambda p: p > threshold and 255)
    return image

def extract_features(image):
    """
    提取图像特征，包括面积、周长、宽高比、上下对称性和左右对称性
    """
    pixels = image.load()
    width, height = image.size
    area = 0
    perimeter = 0
    left_edge = width
    right_edge = 0
    top_edge = height
    bottom_edge = 0

    for x in range(width):
        for y in range(height):
            if pixels[x, y] == 255:
                area += 1
                if x < left_edge:
                    left_edge = x
                if x > right_edge:
                    right_edge = x
                if y < top_edge:
                    top_edge = y
                if y > bottom_edge:
                    bottom_edge = y
                if x > 0 and pixels[x - 1, y] == 0 or y > 0 and pixels[x, y - 1] == 0:
                    perimeter += 1

    width = right_edge - left_edge + 1
    height = bottom_edge - top_edge + 1
    width_height_ratio = width / height if height!= 0 else 0

    top_bottom_symmetry = all(pixels[x, y] == pixels[x, height - y - 1] for x in range(width) for y in range(height // 2))
    left_right_symmetry = all(pixels[x, y] == pixels[width - x - 1, y] for x in range(width // 2) for y in range(height))

    return {
        'area': area,
        'perimeter': perimeter,
        'width_height_ratio': width_height_ratio,
        'top_bottom_symmetry': top_bottom_symmetry,
        'left_right_symmetry': left_right_symmetry
    }

def match_template(features):
    """
    与数字模板进行特征匹配，找到最相似的数字
    """
    min_diff = float('inf')
    recognized_digit = -1

    for digit, template_features in digit_templates.items():
        area_diff = abs(features['area'] - template_features['area'])
        perimeter_diff = abs(features['perimeter'] - template_features['perimeter'])
        width_height_ratio_diff = abs(features['width_height_ratio'] - template_features['width_height_ratio'])
        top_bottom_symmetry_diff = 1 if features['top_bottom_symmetry']!= template_features['top_bottom_symmetry'] else 0
        left_right_symmetry_diff = 1 if features['left_right_symmetry']!= template_features['left_right_symmetry'] else 0

        total_diff = area_diff + perimeter_diff + width_height_ratio_diff + top_bottom_symmetry_diff + left_right_symmetry_diff

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