#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/def/peak.html
作为中国人，实在无法从peak hell想到pickle。
<peakhell src="banner.p"/>
所以谜面的URL是
http://www.pythonchallenge.com/pc/def/banner.p
看起来是一串不知道是什么的字符串。用pickle还原后，是一个list，每个元素还是list，
每个元素是一个字典，从字符映射到数字。这里应该是把每个第二层的list中的key字符串打印value次。
打印出来是channel。
"""
import urllib.request
import pickle

puzzle = 'http://www.pythonchallenge.com/pc/def/banner.p'
with urllib.request.urlopen(puzzle) as response:
    o = pickle.load(response)
    for element in o:
        print("".join([e[0] * e[1] for e in element]))
