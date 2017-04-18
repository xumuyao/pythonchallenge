#!/bin/env python3
# -*- coding:utf-8 -*-
"""http://www.pythonchallenge.com/pc/return/balloons.html

图片找茬，但是图片的不同只有亮度（brightness），所以用brightness换URL，得到
网页注释中的提示：maybe consider deltas.gz，下载地址是
http://www.pythonchallenge.com/pc/return/deltas.gz
这个文件里有一个文件delta.txt，内容是明显分为两栏的代表字节十六进制表示法的数组。
所以用到gzip和difflib。
"""
import gzip
import difflib

with gzip.open('018_deltas.gz') as f:
    raw_lines = f.readlines()

column1 = []
column2 = []

# 解题思路是网上找的：对于第一栏特有的内容，放入第一个png文件，
# 第二栏特有的内容放到第二个png文件，两栏共有的内容则放到第三个png文件。
# 所以先要把一行分成两栏。第一栏有53个字符，下标0到52，第二栏从下标56开始直到最后。
for raw_line in raw_lines:
    line = raw_line.decode('latin1')
    column1.append(line[0:53] + '\n')
    column2.append(line[56:])


def hex_to_bytes(hex_str):
    result = []
    hex_pr = hex_str.split(' ')
    for pr in hex_pr:
        if pr:
            result.append(chr(int(pr, 16)).encode('latin1'))
    return b''.join(result)


diff = difflib.Differ()
d = diff.compare(column1, column2)
# -开始的是第一栏独有的，+开始的是第二栏独有的，空格开始的是共有的。
# 开三个文件，把十六进制数字变成字节写入。
with open('018_c1.png', 'wb') as c1, open('018_c2.png', 'wb') as c2, open('018_common.png', 'wb') as common:
    for delta in d:
        if delta.startswith('-'):
            c1.write(hex_to_bytes(delta[2:-1]))
        elif delta.startswith('+'):
            c2.write(hex_to_bytes(delta[2:-1]))
        elif delta.startswith(' '):
            common.write(hex_to_bytes(delta[2:-1]))

# butter fly ../hex/bin.html
