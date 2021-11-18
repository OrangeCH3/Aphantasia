#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.06 11:30
# @File     : 23-打家劫舍.py
# @Project  : AGTD


# 特殊点：数组收尾相接


class Solution(object):

    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        res1 = self.robRange(nums, 0, n - 1)
        res2 = self.robRange(nums, 1, n)

        return max(res1, res2)

    def robRange(self, nums, start, end):
        # # n为2时的特殊情况
        # if end-1 == start:
        #     return nums[start]

        dp = [0] * len(nums)
        dp[start] = nums[start]
        dp[start + 1] = max(nums[start], nums[start + 1])

        for i in range(start + 2, end):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


if __name__ == '__main__':
    nums = [1, 6, 7, 4]
    solution = Solution()
    res = solution.rob(nums)
    print(res)
