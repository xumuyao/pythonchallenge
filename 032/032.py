#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/arecibo.html
<!-- you are in level 32 -->
Fill in the blanks <!-- for warmup.txt -->
http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/warmup.txt

"Free" as in "Free speech", not as in "free...
beer

这是名为数织（Nonograms）的游戏。
游戏棋盘是一张方形格网，其中的每个格子最终需要涂成红色。 棋盘每一行横线左边列出的数字表示该行上每一组相邻的红色格子的长度。
棋盘每一列竖线上方列出的数字表示该列上每一组相邻的红色格子的长度。 游戏目标是要找出所有的红色方格。
我的解题代码来自这里：https://rosettacode.org/wiki/Nonogram_solver#Python。
"""
import collections
from functools import reduce
try:
    from itertools import izip as zip
except ImportError as ie:
    print('NO izip.')


def read_nonogram(file):
    """从txt文件读取内容，并构造nonogram的描述数据结构。
    返回的应该是包含三个项目的dict，每个item value是列表的列表。
    """
    result = collections.defaultdict(list)
    current = ''
    with open(file, 'r') as input:
        for line in input.readlines():
            line = line.strip()
            if line.startswith('#'):
                current = line.split()[1]
            elif line:
                result[current].append([int(x) for x in line.split()])
    return result


def gen_row(w, s):
    """Create all patterns of a row or col that match given runs."""
    def gen_seg(o, sp):
        if not o:
            return [[2] * sp]
        return [[2] * x + o[0] + tail
                for x in range(1, sp - len(o) + 2)
                for tail in gen_seg(o[1:], sp - x)]

    return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]


def deduce(dimensions, horizontal, vertical):
    """主要解题函数
    [description]
    :param dimensions: 描述nonogram的维度
    :type dimensions: a list of a list
    :param horizontal: nonogram的横向描述，每个list从上到下排列。
    :type horizontal: a list of lists
    :param vertical: nonogram的纵向描述，每个list从左到右排列。
    :type vertical: a list of lists
    :returns: [description]
    :rtype: {[type]}
    """
    def allowable(row):
        return reduce(lambda a, b: [x | y for x, y in zip(a, b)], row)

    def fits(a, b):
        return all(x & y for x, y in zip(a, b))

    def fix_col(n):
        """See if any value in a given column is fixed;
        if so, mark its corresponding row for future fixup."""
        c = [x[n] for x in can_do]
        cols[n] = [x for x in cols[n] if fits(x, c)]
        for i, x in enumerate(allowable(cols[n])):
            if x != can_do[i][n]:
                mod_rows.add(i)
                can_do[i][n] &= x

    def fix_row(n):
        """Ditto, for rows."""
        c = can_do[n]
        rows[n] = [x for x in rows[n] if fits(x, c)]
        for i, x in enumerate(allowable(rows[n])):
            if x != can_do[n][i]:
                mod_cols.add(i)
                can_do[n][i] &= x

    def show_gram(m):
        # If there's 'x', something is wrong.
        # If there's '?', needs more work.
        for x in m:
            print(' '.join('x#.?'[i] for i in x))
        print

    w, h = dimensions[0][0], dimensions[0][1]
    rows = [gen_row(w, x) for x in horizontal]
    cols = [gen_row(h, x) for x in vertical]
    can_do = list(map(allowable, rows))

    # Initially mark all columns for update.
    mod_rows, mod_cols = set(), set(range(w))

    while mod_cols:
        for i in mod_cols:
            fix_col(i)
        mod_cols = set()
        for i in mod_rows:
            fix_row(i)
        mod_rows = set()

    if all(can_do[i][j] in (1, 2) for j in range(w) for i in range(h)):
        print('Solution would be unique')  # but could be incorrect!
    else:
        print('Solution may not be unique, doing exhaustive search:')

    # We actually do exhaustive search anyway. Unique solution takes
    # no time in this phase anyway, but just in case there's no
    # solution (could happen?).
    out = [0] * h

    def try_all(n=0):
        if n >= h:
            for j in range(w):
                if [x[j] for x in out] not in cols[j]:
                    return 0
            show_gram(out)
            return 1
        sol = 0
        for x in rows[n]:
            out[n] = x
            sol += try_all(n + 1)
        return sol

    n = try_all()
    if not n:
        print('No solution.')
    elif n == 1:
        print('Unique solution.')
    else:
        print('Totally {0} solutions.'.format(n))
    print


def solve(nonogram, show=False):
    d = nonogram['Dimensions']
    h = nonogram['Horizontal']
    v = nonogram['Vertical']
    if show:
        print(d)
        print(h)
        print(v)
    deduce(d, h, v)


if __name__ == '__main__':
    nonogram = read_nonogram('warmup.txt')
    solve(nonogram, True)
    nonogram = read_nonogram('up.txt')
    solve(nonogram, True)
