#!/bin/env python3
# -*- coding:utf-8 -*-
"""http://www.pythonchallenge.com/pc/return/italy.html
上一题的答案是555-ITALY，取字母部分小写。

<title>walk around</title>
<img src="italy.jpg"><br>

<!-- remember: 100*100 = (100+99+99+98) + (...  -->
<img src="wire.png" width="100" height="100">
顺时针向内的螺旋
http://www.pythonchallenge.com/pc/return/wire.png
宽10000像素、高1像素的图片，但是显示为100*100，说明要把这个图片按顺时针向内螺旋的顺序，转换成100*100的图片。
从(0,0)开始，横向写100个像素，向下写99个像素，向左写99个像素，向上写98个像素。

一只名为uzi的猫
"""


def next_coordinate(current, width):
    """从current坐标计算下一个坐标。

    用X把矩形分为四个象限。在每个象限，坐标前进的方向不一样。在上象限向右，在右象限向下，在下象限向左，在左象限向上。在象限边界上转向。
    判断在哪个象限：x>=y在上右，x<y在下左。x>=y且width-x>=y在上；x<y且width-y>width-x在左。

    :param current: 当前坐标
    :type current: tuple of two integer
    :param width: 正方形的宽度
    :type width: int
    """
    if width % 2 == 0:
        stop = (int((width - 2) / 2), int(width / 2))
    else:
        stop = (int((width - 1) / 2), int(width - 1 / 2))
    if current == stop:
        return None
    x, y = current
    if x >= y:
        right = width - 1 - x
        if right > y:
            # 继续向右
            return (x + 1, y)
        elif right == y:
            # 向下转
            return (x, y + 1)
        elif y == x:
            # 向左转
            return (x - 1, y)
        else:
            # 继续向下
            return (x, y + 1)
    else:
        bottom = width - 1 - y
        if x > bottom:
            # 向左
            return (x - 1, y)
        elif x == bottom:
            # 向上转
            return (x, y - 1)
        elif y == x + 1:
            # 右转
            return (x + 1, y)
        else:
            # 向上
            return (x, y - 1)

from PIL import Image

current = (0, 0)
width = 100
source = Image.open('014_wire.png')
new = Image.new(source.mode, (width, width))

for i in range(0, width * width):
    pixel = source.getpixel((i, 0))
    new.putpixel(current, pixel)
    current = next_coordinate(current, width)

source.close()
new.save('014_answer.png')
new.close()
