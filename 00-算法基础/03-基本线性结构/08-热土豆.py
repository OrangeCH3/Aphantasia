#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.16 15:27
# @File     : 08-热土豆.py
# @Project  : AGTD


def hotPotato(nameList, num):
    queue = []

    for name in nameList:
        queue.append(name)

    while len(queue) > 1:
        for i in range(num):
            queue.append(queue.pop(0))
        queue.pop(0)

    return queue.pop(0)


if __name__ == '__main__':
    print(hotPotato(["A", "B", "C", "D", "E", "F"], 7))
