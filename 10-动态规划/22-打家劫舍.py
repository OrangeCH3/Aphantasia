#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.05 13:03
# @File     : 22-打家劫舍.py
# @Project  : AGTD


class Solution(object):

    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # dp[i]：考虑下标i（包括i）以内的房屋，最多可以偷窃的金额为dp[i]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    solution = Solution()
    res = solution.rob(nums)
    print(res)
