#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/def/channel.html

提示是<!-- <-- zip -->，不是paypal捐款代码。
这个提示不是用zip函数，而是读取一个zip文件的内容。问题是数据源在哪里？
http://www.pythonchallenge.com/pc/def/channel.zip，下载后看里面的文件，
readme的提示是
welcome to my zipped list.
hint1: start from 90052
hint2: answer is inside the zip
所以先从90052.txt的内容开始，里面的内容是Next nothing is 94191，那么就是根据这个数字，
不断地找下一个，直到找不到数字，那个txt文件的内容就是答案。
答案是Collect the comments.
原来真正的答案不在文件里，在每个文件的注释里。按顺序把文件的注释连起来，是HOCKEY。
但是，http://www.pythonchallenge.com/pc/def/hockey.html还不是最终答案，而是组成HOCKEY
的字符，是oxygen。
"""
import zipfile
import urllib.request
import re
import os

puzzle = 'http://www.pythonchallenge.com/pc/def/channel.zip'
local = '006_channel.zip'

# 下载文件
if not os.path.isfile(local):
    with urllib.request.urlopen(puzzle) as response:
        data = response.read()
        with open(local, 'wb') as output:
            output.write(data)
# 解析文件


def loop(f, nothing, answer):
    comment = f.getinfo(nothing + '.txt').comment.decode()
    answer.append(comment)
    content = f.read(nothing + '.txt').decode()
    m = re.search(r'Next nothing is (\d+)', content)
    if m:
        next = m.group(1)
        loop(f, next, answer)
    else:
        print(content)

f = zipfile.ZipFile(local)
answer = []
loop(f, '90052', answer)
print("".join(answer))
f.close()
