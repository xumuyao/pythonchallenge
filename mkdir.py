#!/bin/env python3
# -*- coding:utf-8 -*-

"""制造目录
目前一共有33关。
"""
import os
import shutil

for i in range(0, 34):
    try:
        os.mkdir(str(i).zfill(3))
    except FileExistsError:
        continue

file_list = os.listdir('.')
for file in file_list:
    if os.path.isfile(file):
        dir = file[0:3]
        if os.path.isdir(dir):
            shutil.move(file, dir)
