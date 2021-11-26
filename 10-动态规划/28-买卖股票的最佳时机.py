#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.08 10:13
# @File     : 28-买卖股票的最佳时机.py
# @Project  : AGTD


# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成k笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution(object):

    def maxProfit(self, k, prices):
        if len(prices) == 0:
            return 0

        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
        for j in range(1, 2 * k, 2):
            dp[0][j] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(1, 2 * k, 2):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] + prices[i])

        return dp[-1][-1]

    def maxProfitDitto(self, k, prices):
        if len(prices) == 0:
            return 0

        dp = [0] * (2 * k + 1)
        for z in range(1, 2 * k, 2):
            dp[z] = -prices[0]

        for i in range(1, len(prices)):
            # for j in range(1, 2 * k + 1):
            #     if j % 2:
            #         dp[j] = max(dp[j], dp[j - 1] - prices[i])
            #     else:
            #         dp[j] = max(dp[j], dp[j - 1] + prices[i])
            for j in range(1, 2 * k, 2):
                dp[j] = max(dp[j], dp[j - 1] - prices[i])
                dp[j + 1] = max(dp[j + 1], dp[j] + prices[i])

        return dp[-1]


if __name__ == '__main__':
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    solution = Solution()
    res = solution.maxProfit(k, prices)
    res1 = solution.maxProfitDitto(k, prices)
    print(res, res1)
