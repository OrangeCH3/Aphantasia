#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.15 16:25
# @File     : 36-最大子序和.py
# @Project  : AGTD


# 给定一个整数数组 nums
# 找到一个具有最大和的连续子数组（子数组最少包含一个元素）
# 返回其最大和。


class Solution(object):

    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = nums[0]
        result = dp[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            result = max(result, dp[i])

        return result, dp


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    res = solution.maxSubArray(nums)
    print(res[0])  # 返回的最大连续子数组的和
    print(res[1])  # 返回的具体dp[]数组
