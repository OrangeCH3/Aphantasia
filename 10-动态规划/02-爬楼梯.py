#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 10:18
# @File     : 02-爬楼梯.py
# @Project  : AGTD


class Solution(object):

    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[:3] = [None, 1, 2]  # n为正整数，不需考虑n为0的初始化情况，且n为0时无对应的物理意义

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp


if __name__ == '__main__':
    n = 10
    solution = Solution()
    res = solution.climbStairs(n)
    print(res)
