#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/return/disproportional.html

<img src="disprop.jpg" width="640" height="480" border="0" usemap="#evil" />
    <map name="evil">
        <area shape="circle" coords="326,177,45" href="../phonebook.php" />
    </map>
phone that <remote /> evil
图片是一个电话机的拨号键盘，在数字5上有一个链接
http://www.pythonchallenge.com/pc/phonebook.php
在浏览器直接打开链接，返回一个格式不正确的XML？
所以不能用普通的打开方式，这是XML-RPC？

"""
import xmlrpc.client

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
# 还记得上一题，Bert is evil! go back!
print(conn.phone("Bert"))
# 结果 555-ITALY
