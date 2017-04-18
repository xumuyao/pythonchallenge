#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/return/bull.html
下载http://www.pythonchallenge.com/pc/return/sequence.txt，回答len(a[30]) = ?
文件内容就是这个
a = [1, 11, 21, 1211, 111221, 
look and say是个什么鬼？
11表示前面一个元素是1个1；21表示前面一个元素是2个1；1211表示前面一个元素是1个2和1个1；
111221表示前面一个元素是1个1、1个2和2个1组成。
"""
import itertools


def look_and_say(sequence):
    """根据“look and say”，计算sequence的对应字符串。

    Look and say算法：将字符串中连续相同的子串统计出来，用“重复次数”+“字符”重新组成一个子串。
    :param sequence: 本身也是根据look and say算出来的字符串。
    :type sequence: string
    """
    it = itertools.groupby(sequence)
    newlist = []
    for key, group in it:
        newlist.append(str(len(list(group))))
        newlist.append(key)
    return "".join(newlist)


def string_at(index):
    """用迭代不用递归，计算位于index位置的look and say。

    [description]
    :param index: [description]
    :type index: [type]
    :returns: [description]
    :rtype: {[type]}
    """
    current = '1'
    if index < 1:
        return current
    else:
        for i in range(0, index):
            current = look_and_say(current)
        return current

# 结果是5808
print(len(string_at(30)))
