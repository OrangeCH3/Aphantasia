#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.31 13:33
# @File     : 04-买卖股票的最佳时机.py
# @Project  : AGTD


class Solution(object):

    def maxProfit(self, prices):
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    res = solution.maxProfit(prices)
    print(res)
