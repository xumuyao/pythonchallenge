#!/bin/env python3
# -*- coding:utf-8 -*-
"""http://www.pythonchallenge.com/pc/return/romance.html
图片是巧克力饼干，但是又嵌了第4关的图片，所以是第四关的URL使用了cookies。
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
里面有cookie内容是info=you+should+have+followed+busynothing...
那么就是说，本关的URL是
http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345
其中的cookie是info=B
"""
import re
import urllib.request
import urllib.parse
import xmlrpc.client
import bz2

# First of all, get the data that is hidden within the "Set-Cookie" headers:
uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={0}"
nn_rep = re.compile("the next busynothing is (\d+)")
cookie_val = re.compile("info=([^;]+);")
result = []
nothing = "12345"

while True:
    response = urllib.request.urlopen(uri.format(nothing))
    next = response.read().decode()
    cookie = response.getheader("Set-Cookie")
    response.close()

    cval = cookie_val.search(cookie)

    if cookie and cval:
        # cookie里是一个字节的URL编码，所以编码格式要用latin-1。
        token = urllib.parse.unquote_plus(cval.group(1), 'latin1')
        print('token是{0}'.format(token))
        result.append(token.encode('latin1'))

    g = nn_rep.search(next)
    if g:
        nothing = g.group(1)
        print('下一个busynothing是{0}'.format(nothing))
    else:
        print('没有下一个busynothing')
        break

bz2_bytes = b''.join(result)
print(bz2.decompress(bz2_bytes).decode('latin1'))
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
# 莫扎特的父亲是Leopold Mozart，所以用第13关的URL来“打电话”。
conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print('获得新的URL提示：')
print(conn.phone("Leopold"))
# 555-VIOLIN
# 新的URL是 http://www.pythonchallenge.com/pc/return/violin.html 但是显示：
# no! i mean yes! but ../stuff/violin.php.
# 所以真正的URL是 http://www.pythonchallenge.com/pc/stuff/violin.php
uri = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = urllib.request.Request(uri, headers={"Cookie": "info=" + urllib.parse.quote_plus(msg)})

print(urllib.request.urlopen(req).read())
"""
<html>
<head>
  <title>it\'s me. what do you want?</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
\t<br><br>
\t<center><font color="gold">
\t<img src="leopold.jpg" border="0"/>
<br><br>
oh well, don\'t you dare to forget the balloons.</font>
</body>
</html>
"""
# http://www.pythonchallenge.com/pc/return/balloons.html
