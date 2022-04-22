#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.16 15:46
# @File     : 10-回文词判定.py
# @Project  : AGTD


def palchecker(str):
    deque = []

    for char in str:
        deque.append(char)

    stillEqual = True

    while len(deque) > 1 and stillEqual:
        first = deque.pop()
        last = deque.pop(0)
        if first != last:
            stillEqual = False

    return stillEqual


if __name__ == '__main__':
    print(palchecker("raatr"))
    print(palchecker("raar"))
