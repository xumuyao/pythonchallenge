#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/return/evil.html
居然还有密码验证，怕是前面有跳关的？huge:file。
<img src="evil1.jpg"><br>
提示：有1，就有2,3,4……
http://www.pythonchallenge.com/pc/return/evil1.jpg 洗牌的图片
http://www.pythonchallenge.com/pc/return/evil2.jpg 显示扩展名是gfx。
http://www.pythonchallenge.com/pc/return/evil3.jpg no more evils
下载 http://www.pythonchallenge.com/pc/return/evil2.gfx 不知道是什么格式的。
http://www.pythonchallenge.com/pc/return/evil4.jpg Bert is evil! go back!
后面就是404了。那么有用的信息在4和1上。
洗牌的图片，牌堆被分成了5份，那么gfx文件也平分成5份，可能会是图片。
我错了，洗牌不是把牌平分，而是轮流分，所以不是把一个块写入，而是每个字节依次写入。
disproportional
"""
import os.path

gfx = '012_evil2.gfx'
size = os.path.getsize(gfx)
block_size = int(size / 5)

with open(gfx, 'rb') as evil:
    data = evil.read()

for y in range(0, 5):
    with open('012_split{0}.jpg'.format(y), 'wb') as split:
        # 这个语法是slice切片。两个冒号隔开三个数字，和Java中的for三个表达式的意义一样：
        # 起始、结束、步进值。
        split.write(data[y::5])
