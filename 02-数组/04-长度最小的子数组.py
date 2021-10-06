#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.09.29 15:52
# @File     : 04-长度最小的子数组.py
# @Project  : AGTD


# 给定一个含有 n 个正整数的数组和一个正整数 s
# 找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度
# 如果不存在符合条件的子数组，返回 0


# 滑动窗口法（双指针）
def min_sublist(s, nums):

    # 定义一个无限大的数字
    res = float("inf")

    the_sum = 0
    index = 0

    for i in range(len(nums)):

        the_sum += nums[i]

        while the_sum >= s:

            res = min(res, i-index+1)
            the_sum -= nums[index]
            index += 1

    if res == float("inf"):
        return 0
    else:
        return res


if __name__ == '__main__':

    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    res = min_sublist(s, nums)
    print(res)
