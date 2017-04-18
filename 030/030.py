#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
<title>relax you are on 30</title>
<img src="yankeedoodle.jpg" border="0"/>
    <br>The picture is only meant to help you relax
         <!-- while you look at the csv file -->
有个csv文件 http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv
8列921行，但是最后一个数字缺了，一共是8*921-1=7367。分解质因数，有
7367=53 x 139，那么这是……53 x 139大小的用flaot来表示像素的图片。
"""
import csv
from PIL import Image

floats = []
with open('yankeedoodle.csv', 'r') as input:
    reader = csv.reader(input)
    for row in reader:
        floats.extend([s.strip() for s in row if s])
with Image.new('F', (53, 139)) as img:
    img.putdata(list(map(float, floats)))
    # 图片需要镜面翻转还要旋转。
    img = img.transpose(Image.ROTATE_90)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save('answer.tiff')

# n=str(x[i])[5] + str(x[i+1])[5] + str(x[i+2])[6]
# 每三个数字一组，从**文本**中读取第6、6、7个字符（是数字），作为字节。
s = [chr(int(floats[i][5] + floats[i + 1][5] + floats[i + 2][6]))
     for i in range(0, len(floats) - 2, 3)]
print(''.join(s))
