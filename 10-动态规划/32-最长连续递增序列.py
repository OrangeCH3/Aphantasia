#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.09 15:21
# @File     : 32-最长连续递增序列.py
# @Project  : AGTD


# 给定一个未经排序的整数数组，找到最长且(连续)递增的子序列，并返回该序列的长度。


class Solution(object):

    # 动态规划
    def findLengthOfLCIS(self, nums):

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1

        return max(dp), dp

    # 贪心
    def findLengthOfLCISDitto(self, nums):
        n = len(nums)

        if n == 0:
            return 0

        result = 1
        count = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1
            result = max(result, count)

        return result


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    solution = Solution()
    res = solution.findLengthOfLCIS(nums)
    res1 = solution.findLengthOfLCISDitto(nums)
    print(res[0])
    print(res[1])
    print(res1)
