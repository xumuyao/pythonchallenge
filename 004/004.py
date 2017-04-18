#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/def/linkedlist.php

谜面是图片链接 http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
点击之后会有新的url。
网页注释中有提示：urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.
所以思路是用urllib向图片包含链接发起连续请求，返回一个字符串，其中有模式and the next nothing is 45439，
从中提取出数字部分，作为新的URL附加到
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=
之后，继续发起get请求，直到满400次。
不到400次有提示
16044
Yes. Divide by two and keep going.
这里要换8022，然后继续？？
在第251次出现答案peak.html。
"""
import urllib.request
import re

baseUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
token = '12345'

for x in range(0, 400):
    with urllib.request.urlopen(baseUrl + token) as response:
        html = response.read().decode()
        print(str(x) + '. ' + html)
        o = re.search(r'the next nothing is (\d+)', html)
        if o:
            token = o.group(1)
            print('The next token is {0}'.format(token))
        else:
            newNumber = int(token) / 2
            token = str(newNumber)
