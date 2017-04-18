#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/ring/grandpa.html
<title>Where am I?</title>
<a href="../rock/grandpa.html"><img src="grandpa.jpg"/></a>
这个照片是什么地方呢？泰国苏梅岛（Koh Samui）阿公石。百度图片搜索还是能用的。
谁能想到用户名密码组合要问什么，问的是地名:国家。全部是小写字母，没有空格。
kohsamui:thailand
<title>UFOs ?</title>
<img src="mandelbrot.gif" border="0">
    <window left="0.34" top="0.57" width="0.036" height="0.027"/>
    <option iterations="128"/>
</img>
利用给出的参数画一幅新图后，和原图比较，存在一些数据不同的点（差值为16和-16），一共有1679个，因式分解为1679=23*73，所以可以再构造一幅新图。
这里有个知乎专栏不错
https://zhuanlan.zhihu.com/p/25792397 曼德勃罗集
"""
from PIL import Image
width = 0.036
height = 0.027
left = 0.34
top = 0.57 + height  # 为什么要加上height？
iterations = 128
imgbase = Image.open('mandelbrot.gif')
img = imgbase.copy()
diff = []
for j in range(imgbase.size[1]):
    for i in range(imgbase.size[0]):
        point0 = complex(left + i * width / imgbase.size[0], top - (1 + j) * height / imgbase.size[1])
        point = 0 + 0j
        for k in range(iterations):
            point = point ** 2 + point0
            if point.imag**2 + point.real**2 > 4:
                break
        img.putpixel((i, j), k)
        if k != imgbase.getpixel((i, j)):
            diff.append(k - imgbase.getpixel((i, j)))
img.save('new1.png')
print(len(diff))
img2 = Image.new('1', (23, 73))
img2.putdata([i < 0 for i in diff])
img2.save('new2.png')
# 图片完全看不清，看解释是这个
# https://en.wikipedia.org/wiki/Arecibo_message
