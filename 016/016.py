#!/bin/env python3
# -*- coding:utf-8 -*-
"""http://www.pythonchallenge.com/pc/return/mozart.html
http://www.pythonchallenge.com/pc/return/mozart.gif
let me get this straight
图片中有一些粉红色的小块块，通过在行上移动像素，使所有的粉红色块块排成一列。
值得注意的是给出的图像是一个索引图像，因此读取图像数据之后的内容不是RGB值，而是索引值，在这幅图像中粉红色对应的索引值是195。
移动方法：将一行从第一个索引值为195的点到最右边的点移动到行首，而点左边的内容移动到右边。
"""

from PIL import Image, ImageChops

# Image.crop(box=None)
# Returns a rectangular region from this image. The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate.
# 在Python3，ASCII大于128的用encode会返回两个字节，因为默认编码是UTF8，这里要用latin1。
# http://www.oschina.net/question/2741863_2199513?fromerr=LU780iPk
magic = chr(195).encode('latin1')
with Image.open('016_mozart.gif') as mozart:
    for y in range(0, mozart.height):
        box = (0, y, mozart.width, y + 1)
        row = mozart.crop(box)
        bytes = row.tobytes()
        i = bytes.find(magic)
        row = ImageChops.offset(row, -i)
        mozart.paste(row, box)
    mozart.save('016_answer.gif')
