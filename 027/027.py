#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/hex/speedboat.html
<title>between the tables</title>
<a href="../ring/bell.html">
<img src="zigzag.jpg"> <!-- did you say gif? -->
</a>
<!-- oh, and this is NOT a repeat of 14 -->
http://www.pythonchallenge.com/pc/hex/zigzag.gif
点击图片链接需要新的认证，所以按提示，图片扩展名改为gif，得到有噪点的图片zigzag.gif。
调色板里是什么？
看别人的攻略，是读取调色板，里面每三个值表示一个索引值，我看过三个值都是一样的，那么就取其中一个。
正好是256个。
调色板的数值才是色彩索引号，所以做一个映射，字节映射到调色板数值所对应的位置。
"""
import math
import bz2
import keyword
from PIL import Image

with Image.open('zigzag.gif') as zigzag:
    # table = zigzag.getpalette()[::3]
    table = zigzag.palette.getdata()[1][::3]
    image_bytes = zigzag.tobytes()
    size = zigzag.size

ascii_table = ''.join([chr(i) for i in range(256)]).encode('latin1')
trans = bytes.maketrans(ascii_table, table)
remapped = image_bytes.translate(trans)
diff = ([], [])
# (1-bit pixels, black and white, stored with one pixel per byte)
with Image.new('1', size, 0) as img:
    offset = 1
    for i in range(offset, len(image_bytes)):
        x = (i - offset) % size[0]
        y = int(math.floor((i - offset) / size[0]))
        lhs = image_bytes[i]
        rhs = remapped[i - offset]
        if lhs != rhs:
            diff[0].append(lhs)
            diff[1].append(rhs)
            img.putpixel((x, y), 1)
    img.save('answer.png')
# not (key) word -- busy?
text = bz2.decompress(''.join(map(chr, diff[0])).encode('latin1'))
# print(text)
# not python (key)word
for word in text.decode().split():
    if not keyword.iskeyword(word):
        print(word)
# 这个题目是根据Python2语法来的，所以print和exec都还是关键字。
# The keyword list is compatible with Python 2, so 'print' and 'exec' are
# still keywords.
# ../ring/bell.html 新的网页认证信息：
# repeat
# switch
