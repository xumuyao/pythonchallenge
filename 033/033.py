#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/beer.html
<title>33 bottles of beer on the wall</title>
<img src="beer1.jpg" border="0"/><br><br>
<!--
If you are blinded by the light,
remove its power, with its might.
Then from the ashes, fair and square,
another truth at you will glare.
-->
真正的题目是http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/beer2.png
在一堆黑白噪点的中心有个灰色的X。
不断地去掉颜色最高的两组点，同时用剩下的点画图，画图时颜色不是最高的点一律作暗色对待。
"""
import math
from PIL import Image

img = Image.open('beer2.png')
f = img.getdata()
color = img.getcolors()
img.close()

for i in range(65, -1, -2):
    s = []
    t = []
    for j in f:
        if j != color[i][1] and j != color[i - 1][1]:
            s.append(j)
            t.append(0)
        else:
            if j == color[i][1]:
                t.append(1)
            else:
                t.append(0)
    f = s
    n = int(math.sqrt(len(t)))
    new = Image.new('1', (n, n))
    new.putdata(t)
    new.save('%d.png' % ((i - 1) / 2))
# snilmerg -> gremlins
