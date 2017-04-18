#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/hex/ambiguity.html
图片是641*641
提示够直接的，从（右）上到（左）下走出迷宫，那么路线就是答案？
黑色是路白色是墙，但是黑色路径上每隔一个像素是深浅不一的红点。所以每路过一个红点，取其R值，就是一个字节。
将所有R值组成的字节写入一个文件……
"""
# 构造迷宫，用二元int list表示：-1表示墙，也就是白色的像素。非白色像素取R通道的值。
# 左上角的数字区域被白色包围了，所以可以放心认为非白色像素都是路。
from PIL import Image


def reachablePoints(_maze, _currPos):
    """在_maze的_currPos位置，返回所有可达的邻近点list。

    返回类型是tuple的list，在maze中，邻近maze的所有可达点的坐标。
    “可达”的意思是没有走过、在maze中点的值大于-1、不会出界。
    这个函数不会改变_maze中的内容。
    :param _maze: 迷宫
    :type _maze: 二维list
    :param _currPos: 当前坐标，第一个是y值，第二个是x值。
    :type _currPos: 二元tuple
    """
    # 围绕currPos四个方向的四个点的坐标
    adjacent = list()
    adjacent.append((_currPos[0], _currPos[1] - 1))
    adjacent.append((_currPos[0], _currPos[1] + 1))
    adjacent.append((_currPos[0] - 1, _currPos[1]))
    adjacent.append((_currPos[0] + 1, _currPos[1]))
    return [p for p in adjacent if canPass(_maze, p)]


def canPass(_maze, position):
    """判断一个坐标在迷宫中是可以走的。

    这个位置可以在迷宫中也可以不在迷宫中。不在迷宫中的自然是不可走的。
    在迷宫中的，position指定的位置是-1。
    :param _maze: 迷宫
    :type _maze: 二维list
    :param position: y坐标，x坐标
    :type position: 二元tuple
    """
    (y, x) = position
    if y < 0 or y < 0:
        return False
    if y >= len(_maze):
        return False
    if x >= len(_maze[y]):
        return False
    return -1 < _maze[y][x] < 256


# list的list，每个list表示的是水平行，所以引用位置用maze[y][x]
with Image.open('maze.png') as source:
    (xlength, ylength) = source.size
    maze = [[-1 if source.getpixel((x, y)) == (255, 255, 255, 255) else source.getpixel((x, y))[0] for x in range(0, xlength)]
            for y in range(0, ylength)]
    # 起点位置和终点位置
    start = (0, xlength - 2)
    end = (ylength - 1, 1)

# 和迷宫具有同样结构的二维list来保存是从哪一个点（坐标）到达该点的（该初始化时将所有的坐标都置为-1）。
trace = [[(-1, -1) for x in range(0, xlength)] for y in range(0, ylength)]
# 一个可以保存坐标的栈。每次将maze能够走通的点（值大于-1）坐标都入栈然后在循环的开始处将栈顶元素弹出保存进currPos（保存坐标的变量）中。
postionStack = [start]
# postionStack中pop出的坐标为currPos，测试其位置四周的像素可达。
# 如果像素可达，则将trace中像素坐标所对应的元素改为currPos，并将这些像素的坐标入栈。
# 将maze中可达像素的位置的值加上256（因为范围是0-255），防止重复测试。
# 最后从trace出口处开始倒序输出所走路径。
while len(postionStack) > 0:
    currPos = postionStack.pop()
    if currPos == end:
        break
    reachable = reachablePoints(maze, currPos)
    if len(reachable) > 0:
        for y, x in reachable:
            trace[y][x] = currPos
            postionStack.append((y, x))
            maze[y][x] += 256

route = [end]
currPos = end
while currPos != start:
    y, x = currPos
    currPos = trace[y][x]
    route.append(currPos)
# 反转route
route.reverse()

# 复原maze，值大于255的要减去256。
for y in range(0, ylength):
    for x in range(0, xlength):
        if maze[y][x] > 255:
            maze[y][x] -= 256

# route中位于偶数位置（但下标是奇数）的坐标提取出来。
red = [position for index, position in enumerate(route) if index % 2 == 1]
# 换算成字节，写入文件。
with open('answer.zip', 'wb') as answer:
    for y, x in red:
        assert maze[y][x] > -1
        b = maze[y][x]
        answer.write(chr(b).encode('latin1'))
# zip中的maze.png是答案，另外一个估计是下一关的谜面。
