#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.09.29 9:44
# @File     : 求x的n次方.py
# @Project  : AGTD

import sys

sys.setrecursionlimit(100000)


# 时间复杂度是O(logn)
def nthx(x, n):

    if n == 0:
        return 1

    t = nthx(x, n//2)  # 将n/2个递归操作抽取出来

    # n为奇数项
    if n % 2 == 1:
        return t*t*x

    # n为偶数项
    else:
        return t*t


if __name__ == '__main__':
    res = nthx(3, 3)
    print(res)
