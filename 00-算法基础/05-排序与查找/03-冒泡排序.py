#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 16:14
# @File     : 03-冒泡排序.py
# @Project  : AGTD


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum -= 1


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(alist)
    print(alist)

    alist1 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    shortBubbleSort(alist1)
    print(alist1)
