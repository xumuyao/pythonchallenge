#!/bin/env python3
# -*- coding:utf-8 -*-

"""接第20关。

20关下载的zip文件是第21关。
"""
# 解压zip文件得到其中的内容。
zipname = '021.zip'
import zipfile
z = zipfile.ZipFile(zipname)
# zip的密码是invader反过来redavni
z.extractall(pwd=b'redavni')
z.close()
# 释放出来的package.pack是个zlib文件。
import zlib
import bz2

with open('package.pack', 'rb') as libfile:
    data = zlib.decompress(libfile.read())

# We used to play this game when we were kids
# When I had no idea what to do, I looked backwards.
logs = ''
while True:
    if data[:2] == b'\x78\x9c':  # 开头两个字符十六进制，也可以写成b'x\x9c'，因为‘x'的十六进制为\x78
        data = zlib.decompress(data)
        logs += ' '
    elif data[:2] == b'\x42\x5a':  # bz2文件开头十六进制， 表示：BZ
        data = bz2.decompress(data)
        logs += '#'
    elif data[-2:] == b'\x9c\x78':  # 这个来自于第二个提示：往回看就代表反向操作
        data = zlib.decompress(data[::-1])
        logs += '\n'
    else:
        break

print(data[::-1])
print(logs)
# copper
