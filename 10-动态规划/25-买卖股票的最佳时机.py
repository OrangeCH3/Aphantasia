#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.07 11:43
# @File     : 25-买卖股票的最佳时机.py
# @Project  : AGTD


# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


class Solution(object):

    def maxProfit(self, prices):
        length = len(prices)
        if length == 0:
            return 0

        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

        return dp[-1][-1]

    def maxProfitDitto(self, prices):
        length = len(prices)
        if length == 0:
            return 0

        dp = [[0] * 2 for _ in range(2)]  # 这里只开辟了一个2*2大小的二维数组
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, length):
            dp[i % 2][0] = max(dp[(i - 1) % 2][0], -prices[i])
            dp[i % 2][1] = max(dp[(i - 1) % 2][1], prices[i] + dp[(i - 1) % 2][0])

        return dp[(length - 1) % 2][-1]


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4, 8]
    solution = Solution()
    res = solution.maxProfit(prices)
    res1 = solution.maxProfitDitto(prices)
    print(res, res1)
