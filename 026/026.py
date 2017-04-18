#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://butter"fly@www.pythonchallenge.com/pc/hex/decent.html
<title>be a man - apologize!</title>
<img src="decent.jpg"> <!-- you've got his e-mail -->
Hurry up, I'm missing the boat
出现了sorry音频的第19关，一封来自leopold.moz@pythonchallenge.com的邮件，那么回信就是这个地址，主题就是sorry。
发邮件要用自己的账号，所以我就不用代码，而是直接贴回信内容了。
Have you found my broken zip?
md5: bbb8b499a0eef99b52c7f13f4e78c24b
Can you believe what one mistake can lead to?
第24关的答案里有个文件mybroken.zip，邮件里的md5就是这个邮件正确的校验和，而这个文件错了一个字节。
所以要试出这个字节。
"""
import hashlib

correct_md5 = 'bbb8b499a0eef99b52c7f13f4e78c24b'
with open('mybroken.zip', 'rb') as broken:
    stream = broken.read()
    for i in range(0, len(stream)):
        for j in range(0, 256):
            nextbytes = stream[:i] + chr(j).encode('latin1') + stream[i + 1:]
            md5 = hashlib.md5()
            md5.update(nextbytes)
            if md5.hexdigest() == correct_md5:
                with open('mybroken_new.zip', 'wb') as output:
                    output.write(nextbytes)
                break
# 图片里是speed，但是还有一个提示没有用到：Hurry up, I'm missing the boat，所以合起来是speedboat。