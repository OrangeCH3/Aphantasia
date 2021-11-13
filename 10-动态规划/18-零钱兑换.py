#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.04 10:02
# @File     : 18-零钱兑换.py
# @Project  : AGTD


class Solution(object):

    def coinChange(self, coins, amount):
        # 即使用面额最小1组合，组成amount金额最多使用amount个，因此dp[j] < amount + 1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[-1] if dp[-1] < amount + 1 else -1


if __name__ == '__main__':
    coins = [1, 2, 3, 4, 5, 6]
    amount = 11
    solution = Solution()
    res = solution.coinChange(coins, amount)
    print(res)
