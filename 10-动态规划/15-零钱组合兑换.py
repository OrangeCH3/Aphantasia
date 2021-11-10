#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.04 9:31
# @File     : 15-零钱组合兑换.py
# @Project  : AGTD


class Solution(object):

    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1

        # 求组合数就是外层for循环遍历物品，内层for遍历背包
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]

        return dp[amount]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    solution = Solution()
    res = solution.change(amount, coins)
    print(res)
