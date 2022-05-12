#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 16:31
# @File     : 05-插入排序.py
# @Project  : AGTD


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentvalue


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(alist)
    print(alist)
