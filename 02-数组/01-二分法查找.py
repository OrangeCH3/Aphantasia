#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.09.29 10:44
# @File     : 01-二分法查找.py
# @Project  : AGTD


# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
# 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1


# 左闭右闭版本
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:

        middle = (left + right) // 2

        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            return middle

    return -1


if __name__ == '__main__':
    nums = [-1, 0, 2, 3, 5, 9, 12]
    target = 9

    res = binary_search(nums, target)
    print(res)
