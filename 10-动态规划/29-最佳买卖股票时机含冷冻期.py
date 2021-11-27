#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.08 10:52
# @File     : 29-最佳买卖股票时机含冷冻期.py
# @Project  : AGTD


# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格。
# 设计一个算法计算出最大利润。在满足以下约束条件下。
# 你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 1. 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 2. 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。


# dp[i][j]，第i天状态为j，所剩的最多现金为dp[i][j]
# 1. 状态一：买入股票状态（今天买入股票，或者是之前就买入了股票然后没有操作）
#
# 卖出股票状态，这里就有两种卖出股票状态
# 2. 状态二：两天前就卖出了股票，度过了冷冻期，一直没操作，今天保持卖出股票状态
# 3. 状态三：今天卖出了股票
#
# 4. 状态四：今天为冷冻期状态，但冷冻期状态不可持续，只有一天！


class Solution(object):

    def maxProfit(self, prices):
        n = len(prices)

        if n == 0:
            return 0

        dp = [[0] * 4 for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][1], dp[i - 1][3]) - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]

        return max(dp[-1][:]), dp


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    solution = Solution()
    res = solution.maxProfit(prices)
    print(res[0])
    print(res[1])
