#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.07 15:00
# @File     : 26-买卖股票的最佳时机.py
# @Project  : AGTD


# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution(object):

    def maxProfit(self, prices):
        length = len(prices)

        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])  # 注意这里是和25-买卖股票的最佳时机唯一不同的地方
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

        return dp[-1][-1]

    def maxProfitDitto(self, prices):
        length = len(prices)

        dp = [[0] * 2] * 2
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, length):
            dp[i % 2][0] = max(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1] - prices[i])
            dp[i % 2][1] = max(dp[(i - 1) % 2][1], dp[(i - 1) % 2][0] + prices[i])

        return dp[(length - 1) % 2][1]


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    res = solution.maxProfit(prices)
    res1 = solution.maxProfitDitto(prices)
    print(res, res1)
