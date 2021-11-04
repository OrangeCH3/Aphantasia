#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 17:05
# @File     : 17-买卖股票的最佳时机含手续费.py
# @Project  : AGTD


# 情况一：收获利润的这一天并不是收获利润区间里的最后一天（不是真正的卖出，相当于持有股票），所以后面要继续收获利润。
# 情况二：前一天是收获利润区间里的最后一天（相当于真正的卖出了），今天要重新记录最小价格了。
# 情况三：不作操作，保持原有状态（买入，卖出，不买不卖）


class Solution(object):

    def maxProfit(self, prices, fee):

        result = 0
        minPrice = prices[0]

        for i in range(1, len(prices)):

            # 情况二：相当于买入
            if prices[i] < minPrice:
                minPrice = prices[i]
            # 情况三：保持原有状态（因为此时买则不便宜，卖则亏本）
            elif minPrice <= prices[i] <= minPrice + fee:
                continue
            # 计算利润，可能有多次计算利润，最后一次计算利润才是真正意义的卖出
            else:
                result += prices[i] - minPrice - fee
                minPrice = prices[i] - fee  # // 情况一，这一步很关键

        return result


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    solution = Solution()
    res = solution.maxProfit(prices, fee)
    print(res)
