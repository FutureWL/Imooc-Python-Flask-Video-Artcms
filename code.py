# coding:utf8
import os
import uuid
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class Code:
    # 随机一个字母或者数字s
    def random_chr(self):
        num = random.randint(1, 3)
        if num == 1:
            # 随机一个 0 到 9 的数字
            char = random.randint(48, 57)
        elif num == 2:
            # 随机一个 a 到 z 的字母
            char = random.randint(97, 122)
        else:
            # 随机一个 A 到 Z 的字母
            char = random.randint(65, 90)
        return chr(char)

    # 随机一个干扰字符
    def random_dis(self):
        arr = ["^", "_", "-", ".", "~"]
        return arr[random.randint(0, len(arr) - 1)]

    # 定义干扰字符颜色，三原色 RGB 0～255
    def random_color1(self):
        return (
            random.randint(64, 255),
            random.randint(64, 255),
            random.randint(64, 255)
        )

    # 定义字符颜色，三原色 RGB 0～255
    def random_color2(self):
        return (
            random.randint(32, 127),
            random.randint(32, 127),
            random.randint(32, 127)
        )

    # 生成验证码
    def create_code(self):
        width = 240
        height = 60
        # 创建一个图片
        image = Image.new("RGB", (width, height), (192, 192, 192))
        # image.show()
        # 创建 font 对象，定义字体和大小
        font_name = random.randint(1, 3)
        font_file = os.path.join(os.path.dirname(__file__), "static/fonts") + "/%d.ttf" % font_name
        font = ImageFont.truetype(font_file, 30)
        # 创建 draw，填充像素点
        draw = ImageDraw.Draw(image)
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                draw.point((x, y), fill=self.random_color1())
        # 填充干扰字符
        for v in range(0, width, 30):
            dis = self.random_dis()
            w = 5 + v
            # 距离图片上边距最多15个像素，最低5个像素
            h = random.randint(5, 15)
            draw.text((w, h), dis, font=font, fill=self.random_color1())
        # 填充字符
        chars = ""
        for v in range(4):
            c = self.random_chr()
            chars += str(c)
            # 随机距离图片上边距高度，最多15px，最低5px
            h = random.randint(5, 15)
            # 占图片宽度1/4，10px间隙
            w = width / 4 * v + 10
            draw.text((w, h), c, font=font, fill=self.random_color2())
        # 模糊效果
        image.filter(ImageFilter.BLUR)
        image_name = "%s.jpg" % uuid.uuid4().hex
        save_dir = os.path.join(os.path.dirname(__file__), "static")
        save_dir += "/code"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        image.save(save_dir + "/" + image_name, "jpeg")
        return dict(
            img_name=image_name,
            code=chars
        )


if __name__ == '__main__':
    c = Code()
    # print (c.random_chr())
    # print (c.random_dis())
    # print (c.random_color1())
    # print (c.random_color2())
    c.create_code()
