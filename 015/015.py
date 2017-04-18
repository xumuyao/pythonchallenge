#!/bin/env python3
# -*- coding:utf-8 -*-

"""http://www.pythonchallenge.com/pc/return/uzi.html

1*6年1月26日周一，第二天是某人的生日。这一年的二月还是闰月。
<!-- he ain't the youngest, he is the second -->
问，谁在1*6年1月27日周二出生？
106到1996年，10年步进，而且必须是4的倍数。
[156, 376, 556, 776, 956, 1176, 1356, 1576, 1756, 1976]
倒数第二个年份，所以是1756年1月27日周二。莫扎特 mozart
"""
from calendar import weekday
years = [x for x in range(106, 2006, 10) if x % 4 == 0 and weekday(x, 1, 27) == 1]
print(years)
