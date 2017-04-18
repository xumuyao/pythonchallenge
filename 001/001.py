#!/bin/env python
# -*- coding:utf-8 -*-

"""Python Challenge 1
http://www.pythonchallenge.com/pc/def/map.html

everybody thinks twice before solving this.

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

K->M
O->Q
E->G
把上面这一段字符串的每个字母，按字母表顺序向后移动两位。
用到一组不怎么常见的string函数：maketrans和translate
答案是
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
"""

puzzle = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
intable = 'abcdefghijklmnopqrstuvwxyz'
outtable = 'cdefghijklmnopqrstuvwxyzab'
# 更优雅的方式：
# str.maketrans(str.ascii_lowercase, str.ascii_lowercase[2:] + str.ascii_lowercase[:2])
trantab = str.maketrans(intable, outtable)
print(puzzle.translate(trantab))
