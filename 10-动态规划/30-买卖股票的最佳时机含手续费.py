#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.09 14:50
# @File     : 30-买卖股票的最佳时机含手续费.py
# @Project  : AGTD


# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 返回获得利润的最大值。


class Solution(object):

    def maxProfit(self, prices, fee):
        n = len(prices)

        if n == 0:
            return 0

        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)

        return dp[-1][-1], dp


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    solution = Solution()
    res = solution.maxProfit(prices, fee)
    print(res[0])
    print(res[1])
