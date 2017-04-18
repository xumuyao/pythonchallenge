#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/hex/copper.html
<title>emulate</title>
<img src="level22.jpg"><br>
<!-- or maybe white.gif would be more bright-->
人家说这个gif上有白色的点在移动，我看了好几个github上的副本，都没有看出什么，就是一张黑色图片。
每一帧几乎所有点的索引（注意不是像素）都是0，只有一个点例外，是8，所以把这个点的位置集中到一个帧上，就是答案。
"""
from PIL import Image
from PIL import ImageDraw
from PIL import ImageSequence

with Image.open('white.gif') as im:
    with Image.new('RGB', im.size) as new:
        draw = ImageDraw.Draw(new)
        cx, cy = 0, 0
        for frame in ImageSequence.Iterator(im):
            left, upper, right, lower = im.getbbox()
            dx = left - im.size[0] / 2
            dy = upper - im.size[1] / 2
            cx += dx
            cy += dy
            if dx == dy == 0:
                cx += 25
                cy += 25
            if cx:
                draw.point([cx, cy])
        # new.show()
        new.save('answer.png')
# bonus
