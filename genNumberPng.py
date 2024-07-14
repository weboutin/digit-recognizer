from PIL import Image, ImageDraw, ImageFont

def generate_high_quality_digit_image(digit, size=(56, 56), font_size=40):
    # 创建空白图像
    image = Image.new('L', size, color=0)  
    draw = ImageDraw.Draw(image)

    # 选择字体和字体大小
    font = ImageFont.truetype("arial.ttf", font_size)

    # 根据数字绘制
    if digit == 0:
        draw.text((5, 5), "0", font=font, fill=255)
    elif digit == 1:
        draw.text((10, 5), "1", font=font, fill=255)
    elif digit == 2:
        draw.text((5, 5), "2", font=font, fill=255)
    elif digit == 3:
        draw.text((5, 5), "3", font=font, fill=255)
    elif digit == 4:
        draw.text((5, 5), "4", font=font, fill=255)
    elif digit == 5:
        draw.text((5, 5), "5", font=font, fill=255)
    elif digit == 6:
        draw.text((5, 5), "6", font=font, fill=255)
    elif digit == 7:
        draw.text((5, 5), "7", font=font, fill=255)
    elif digit == 8:
        draw.text((5, 5), "8", font=font, fill=255)
    elif digit == 9:
        draw.text((5, 5), "9", font=font, fill=255)

    image.save(f'example2/digit_{digit}.png')

# 生成 0 - 9 的数字图片
for digit in range(10):
    generate_high_quality_digit_image(digit)