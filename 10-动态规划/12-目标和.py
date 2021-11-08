#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.03 10:37
# @File     : 12-目标和.py
# @Project  : AGTD


class Solution(object):

    def findTargetSumWays(self, nums, target):
        sum_value = sum(nums)
        if abs(target) > sum_value or (sum_value + target) % 2 == 1:
            return 0

        bag_size = (sum_value + target) // 2
        dp = [0] * (bag_size + 1)

        dp[0] = 1

        for i in range(len(nums)):
            for j in range(bag_size, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[bag_size]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    solution = Solution()
    res = solution.findTargetSumWays(nums, target)
    print(res)
