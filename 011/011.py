#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/return/5808.html

<html>
<head>
  <title>odd even</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
    <br><br>
    <center>
    <img src="cave.jpg" width="640" height="480" border="0"/>
    <br>
    <br>
    <font color="gold" size="+1"></font>
</body>
</html>
提示够直接，下载图片，提取坐标都是奇数和都是偶数的像素点，重新组成两个新图像。
两张图片上都有evil。
"""
from PIL import Image

img_source = '011_cave.jpg'
with Image.open(img_source) as source:
    width = round(source.width / 2)
    height = round(source.height / 2)
    odd_image = Image.new(source.mode, (width, height))
    even_image = Image.new(source.mode, (width, height))
    # 奇数坐标和偶数坐标
    for x in range(0, width):
        for y in range(0, height):
            odd_image.putpixel((x, y), source.getpixel((x * 2 + 1, y * 2 + 1)))

    for x in range(0, width):
        for y in range(0, height):
            even_image.putpixel((x, y), source.getpixel((x * 2, y * 2)))

    odd_image.save('011_odd.jpg')
    even_image.save('011_even.jpg')
