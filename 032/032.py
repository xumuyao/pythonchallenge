#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/arecibo.html
<!-- you are in level 32 -->
Fill in the blanks <!-- for warmup.txt -->
http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/warmup.txt

这是名为数织（Nonograms）的游戏。
游戏棋盘是一张方形格网，其中的每个格子最终需要涂成红色。 棋盘每一行横线左边列出的数字表示该行上每一组相邻的红色格子的长度。
棋盘每一列竖线上方列出的数字表示该列上每一组相邻的红色格子的长度。 游戏目标是要找出所有的红色方格。
"""
import collections


def read_nonogram(file):
    result = collections.defaultdict(list)
    current = ''
    with open(file, 'r') as input:
        for line in input.readlines():
            line = line.strip()
            if line.startswith('#'):
                current = line[2:]
            elif line:
                result[current].append(line.split())
    return result

nonogram = read_nonogram('warmup.txt')
print(nonogram['Dimensions'])
print(nonogram['Horizontal'])
print(nonogram['Vertical'])
