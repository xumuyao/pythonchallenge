#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/hex/bonus.html
<!--
TODO: do you owe someone an apology? now it is a good time to
tell him that you are sorry. Please show good manners although
it has nothing to do with this level.
-->
<title>what is this module?</title>
<img src="bonus.jpg">
<!--    it can't find it. this is an undocumented module. -->
<!--
'va gur snpr bs jung?'
-->
this是一个没有文档的模块……this的文本用了凯撒密码，也就是字母表移位。
Gur Mra bs Clguba = The Zen of Python。所以这里就用this中的位移方式。
"""
#import this
s = 'va gur snpr bs jung?'
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
# in the face of what?
import this
# ambiguity
