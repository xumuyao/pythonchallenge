#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/def/oxygen.html
谜面就在图片里：http://www.pythonchallenge.com/pc/def/oxygen.png
这个图片里有一条灰色的色带。
PIL（Python Image Library）可用于处理图片。来自廖雪峰的说明：
由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。
所以用pillow而不是PIL。
这一条灰色色带的左上位置是(0,43)，左下位置是(0,61)，右上位置是(607,43)。这个色带在竖直方向上不变色，而在水平方向上每隔7个像素变色，
所以认为，其水平方向上的颜色值(rer,green,blue,alpha)中的一个值（rgb三个值相同）
最终答案：integrity
"""
import re
from PIL import Image

im = Image.open('007_oxygen.png')
# 灰色的特征是RGB三值一样，所以如果不知道色带有多宽，那么可以用r==g==b来判断。
row = [im.getpixel((i, 43)) for i in range(0, 607, 7)]
values = [red for red, green, blue, alpha in row if red == green == blue]
# print(values)
# values中的值理论上范围在0到255之间，观察下来，都小于127，所以认为这些实际代表一个字节。
response = ''.join([b for b in map(chr, values)])
print(response)
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
o = [b for b in map(int, re.findall('\d+', response))]
# print(o)
response = ''.join([b for b in map(chr, o)])
print(response)
