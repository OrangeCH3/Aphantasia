#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 9:31
# @File     : 04-汉诺塔TowerOfHanoi.py
# @Project  : AGTD


# 汉诺塔递归解法
def moveHanoi(height, one, two, three):
    if height >= 1:
        moveHanoi(height - 1, one, three, two)
        moveDisk(height, one, three)
        moveHanoi(height - 1, two, one, three)


def moveDisk(disk, begin, end):
    print(f"Moving disk[{disk}] from {begin} to {end}")


if __name__ == '__main__':
    moveHanoi(3, "Pole-1", "Pole-2", "Pole-3")
