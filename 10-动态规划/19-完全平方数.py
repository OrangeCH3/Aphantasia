#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.04 14:43
# @File     : 19-完全平方数.py
# @Project  : AGTD


class Solution(object):

    def numSquares(self, n):
        nums = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]
        dp = [10 ** 4 + 1] * (n + 1)
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(nums[i], n + 1):
                dp[j] = min(dp[j], dp[j - nums[i]] + 1)

        return dp[-1]


if __name__ == '__main__':
    n = 15
    solution = Solution()
    res = solution.numSquares(n)
    print(res)
