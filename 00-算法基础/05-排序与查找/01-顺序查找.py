#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 11:06
# @File     : 01-顺序查找.py
# @Project  : AGTD


# 无序表顺序查找
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


# 有序表顺序查找
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


if __name__ == '__main__':
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))

    testlist1 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(orderedSequentialSearch(testlist1, 3))
    print(orderedSequentialSearch(testlist1, 13))
