#!/bin/env python3
# -*- coding:utf-8 -*-
"""http://www.pythonchallenge.com/pc/hex/idiot2.html
http://www.pythonchallenge.com/pc/hex/unreal.jpg
线索在其response headers中，在Chrome开发者工具里看其内容是
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Range: bytes 0-30202/2123456789
Transfer-Encoding: chunked
Date: Wed, 05 Apr 2017 04:52:43 GMT
Server: lighttpd/1.4.35
其中突兀的是Content-Range: bytes 0-30202/2123456789。
一般断点下载时才用到 Range 和 Content-Range 实体头。
Range
用于请求头中，指定第一个字节的位置和最后一个字节的位置，一般格式：
Range:bytes=(first byte pos)-[last byte pos]

Content-Range
用于响应头，指定整个实体中的一部分的插入位置，他也指示了整个实体的长度。在服务器向客户返回一个部分响应，它必须描述响应覆盖的范围和整个实体长度。一般格式：
Content-Range: bytes (first byte pos) - [last byte pos]/[entity legth]

在向这个图片发送GET请求时，设置Request Header中的Range。
如果在请求头部中，把Range设置为30203会怎么样呢？
"""
# 用requests吧！
import re
import os
import requests

pattern = r'bytes (\d+)-(\d*)/(\d+)'
regex = re.compile(pattern)

unreal = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
auth = ('butter', 'fly')
range_header = 'bytes={0}-{1}'


def next_invade(start, end):
    headers = {'Range': range_header.format(start, end)}
    r = requests.get(unreal, auth=auth, headers=headers)
    # print(r.status_code)
    # print(r.headers)
    print(r.content)
    cr = r.headers.get('Content-Range')
    if cr:
        mo = regex.search(cr)
        if mo:
            print('{0} {1} {2}'.format(mo.group(1), mo.group(2), mo.group(3)))
            return (r.content.decode(), int(mo.group(2)) + 1)
    r.close()
    return None


ni = next_invade(30203, '')
while ni:
    ni = next_invade(ni[1], '')

# 到30347就没有了。换2123456789
ni = next_invade(2123456789, '')
# 字符串反转要用切片……
print(ni[0][::-1])
# the password is your new nickname in reverse
# 2123456744 2123456788 2123456789
ni = next_invade(2123456743, '')
# and it is hiding at 1152983631
# 意思是从这个位置开始有奇怪的东西可以下载。
headers = {'Range': range_header.format(1152983631, '')}
# 用get下载加stream=True
zipname = '../021.zip'
if os.path.isfile(zipname):
    r = requests.get(unreal, auth=auth, headers=headers, stream=True)
    with open(zipname, 'wb') as f:
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
    r.close()
