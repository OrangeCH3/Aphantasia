#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.08 9:43
# @File     : 27-买卖股票的最佳时机.py
# @Project  : AGTD


# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution(object):

    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

        return dp[-1][-1]

    def maxProfitDitto(self, prices):
        if len(prices) == 0:
            return 0

        dp = [0] * 5
        dp[1] = -prices[0]
        dp[3] = -prices[0]

        for i in range(1, len(prices)):
            dp[1] = max(dp[1], dp[0] - prices[i])
            dp[2] = max(dp[2], dp[1] + prices[i])
            dp[3] = max(dp[3], dp[2] - prices[i])
            dp[4] = max(dp[4], dp[3] + prices[i])

        return dp[-1]


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    solution = Solution()
    res = solution.maxProfit(prices)
    res1 = solution.maxProfitDitto(prices)
    print(res, res1)
