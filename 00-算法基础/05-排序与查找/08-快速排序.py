#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 16:41
# @File     : 08-快速排序.py
# @Project  : AGTD


# 快速排序
def quickSort(nums):
    quickSortHelper(nums, 0, len(nums) - 1)


def quickSortHelper(nums, first, last):
    if first < last:
        splitPoint = partition(nums, first, last)
        quickSortHelper(nums, first, splitPoint - 1)
        quickSortHelper(nums, splitPoint + 1, last)


def partition(nums, first, last):
    poiotValue = nums[first]

    left, right = first + 1, last

    done = False
    while not done:

        while left <= right and nums[left] <= poiotValue:
            left += 1
        while right >= left and nums[right] >= poiotValue:
            right -= 1

        if right < left:
            done = True

        else:
            nums[left], nums[right] = nums[right], nums[left]

    nums[right], nums[first] = nums[first], nums[right]

    return right


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort(alist)
    print(alist)
