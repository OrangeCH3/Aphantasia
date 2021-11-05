#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 12:03
# @File     : 03-使用最小花费爬楼梯.py
# @Project  : AGTD


class Solution(object):

    def minCostClimbingStairs(self, cost):
        lenth = len(cost)
        dp = [0] * lenth
        dp[:2] = cost[:2]

        for i in range(2, lenth):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[lenth - 1], dp[lenth - 2]), dp


if __name__ == '__main__':
    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    solution = Solution()
    res1 = solution.minCostClimbingStairs(cost1)
    res2 = solution.minCostClimbingStairs(cost2)
    print(res1)
    print(res2)
