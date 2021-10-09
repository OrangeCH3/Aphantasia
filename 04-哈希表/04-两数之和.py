#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.08 14:39
# @File     : 04-两数之和.py
# @Project  : AGTD


# 给定一个整数数组 nums 和一个目标值 target。
# 请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。


class Solution:

    def twoSum(self, nums, target):

        records = dict()

        for index, value in enumerate(nums):
            # key not in dict
            if target-value not in records:
                records[value] = index
            # key in dict
            else:
                return [records[target-value], index]


if __name__ == '__main__':

    nums = [2, 7, 11, 46, 29]
    target = 36

    s = Solution()
    res = s.twoSum(nums, target)
    print(res)



