#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/ring/bell.html
<title>many pairs ring-ring</title>
<img src="bell.png" border="0"/>
<br>RING-RING-RING
<br>say it out loud</font>
"""
from PIL import Image
img = Image.open('bell.png')
img.load()
r, g, b = img.split()

gdata = list(g.getdata())
newlist = [(gdata[i] - gdata[i + 1]) for i in range(0, len(gdata), 2)]
s = ''
for i in newlist:
    if i != -42 and i != 42:
        s += chr(abs(i))
print(s)
# whodunnit().split()[0]
# 谁是Python的作者？
