#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 16:38
# @File     : 07-归并排序.py
# @Project  : AGTD


# 归并排序
def mergeSort(nums):
    # 递归结束条件
    if len(nums) <= 1:
        return nums

    # 分解问题，并递归调用
    middle = len(nums) // 2
    left = mergeSort(nums[:middle])
    right = mergeSort(nums[middle:])

    # 合并左右半部，完成排序
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)

    return merged


if __name__ == '__main__':
    alist = [54, 23, 56, 76, 89, 97, 12, 39]
    result = mergeSort(alist)
    print(result)
