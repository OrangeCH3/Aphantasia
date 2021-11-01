#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.31 12:48
# @File     : 03-最大子序和.py
# @Project  : AGTD


class Solution(object):

    def maxSubArray(self, nums):

        maxResult = -float("inf")
        tmpResult = 0

        for i in range(len(nums)):
            tmpResult += nums[i]

            if tmpResult > maxResult:
                maxResult = tmpResult

            if tmpResult <= 0:
                tmpResult = 0

        return maxResult


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    res = solution.maxSubArray(nums)
    print(res)
