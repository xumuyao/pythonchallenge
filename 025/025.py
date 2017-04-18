#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/hex/lake.html
<title>imagine how they sound</title>
<img src="lake1.jpg"> <!-- can you see the waves? -->
不是图片是wave，也就是声音文件。图片一共有25片拼图，所以wav文件有25个。
http://www.pythonchallenge.com/pc/hex/lake1.wav...
"""
import requests
import os.path
import wave
from PIL import Image

for i in range(1, 26):
    local = 'lake%d.wav' % i
    if not os.path.isfile(local):
        url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/lake%d.wav' % i
        r = requests.get(url, stream=True)
        with open(local, 'wb') as f:
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)

# 读取一个文件看看其特点
# frame rate=9600, channels=1, frames=10800
with wave.open('lake1.wav', 'rb') as w1:
    print(w1.getframerate())
    print(w1.getnchannels())
    print(w1.getnframes())

# 10800字节，要是转换为正方形图片，那么就是60*60，因为一个像素需要3字节。
new = []
for i in range(1, 26):
    with wave.open('lake%d.wav' % i, 'rb') as f:
        new.append(Image.frombytes('RGB', (60, 60), (f.readframes(f.getnframes()))))

# 拼图，5*5方式把25个图片合成为一个。
img = Image.new('RGB', (300, 300))
for x in range(5):
    for y in range(5):
        img.paste(new[x * 5 + y], (y * 60, x * 60))
img.save('lake.png')
