#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/ring/guido.html
网页源码中的文字没有什么用，但是有很多只有空格的行，空格数量还不一样。那么空格的数量就表示一个字节。
"""
import requests
import bz2

auth = ('repeat', 'switch')
r = requests.get('http://www.pythonchallenge.com/pc/ring/guido.html', auth=auth)
text = r.content.decode()
r.close()
# 提取全部是空格的行
lines = text.splitlines(False)[12::]
stream = b''
for line in lines:
    bytecode = chr(len(line)).encode('latin1')
    stream += bytecode

print(stream)
# BZh91AY...
print(bz2.decompress(stream))
# "Isn't it clear? I am yankeedoodle!"
