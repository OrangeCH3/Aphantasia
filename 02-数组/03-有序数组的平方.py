#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.09.29 15:39
# @File     : 03-有序数组的平方.py
# @Project  : AGTD


# 给你一个按非递减顺序排序的整数数组 nums
# 返回每个数字的平方组成的新数组，要求也按非递减顺序排序

# 双指针法
def ordered_list_pow2(nums):

    n = len(nums)

    i, j, k = 0, n-1, n-1
    ans = [0] * n

    while i <= j:

        lm = nums[i] ** 2
        rm = nums[j] ** 2

        if lm > rm:
            ans[k] = lm
            i += 1
        else:
            ans[k] = rm
            j -= 1

        k -= 1

    return ans


if __name__ == '__main__':

    nums = [-4, -1, 0, 2, 3, 10]
    res = ordered_list_pow2(nums)
    print(res)

