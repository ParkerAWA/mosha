import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def check_code(width=120, height=30, char_length=5, font_file='H-TTF-BuMing-B-2.ttf', font_size=20):
    code = []
    img = Image.new(mode='RGBA', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGBA')

    def rndChar():
        """
        生成随机字母
        :return:
        """
        return chr(random.randint(65, 90))
        # 生成随机字母
        # return str(random.randint(0, 9))
        # 生成随机数字

    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return random.randint(0, 255), random.randint(10, 255), random.randint(64, 255)

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 10)
        draw.text([i * width / char_length, h], char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰线
    for i in range(5):
        x = random.randint(0, width)
        y = random.randint(0, height)
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        draw.line((x, y, x1, y1), fill=rndColor())

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)
