#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.03 12:36
# @File     : 14-完全背包.py
# @Project  : AGTD


class Solution(object):

    # 先遍历物品，再遍历背包
    def completePack(self, bagLoad, weight, value):
        dp = [0] * (bagLoad + 1)

        for i in range(len(weight)):
            for j in range(weight[i], bagLoad + 1):
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        return dp[bagLoad]

    # 先遍历背包，再遍历物品
    def completePackDitto(self, bagLoad, weight, value):
        dp = [0] * (bagLoad + 1)

        for j in range(bagLoad + 1):
            for i in range(len(weight)):
                if j >= weight[i]:
                    dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        return dp[bagLoad]


if __name__ == '__main__':
    bagLoad = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    solution = Solution()
    res1 = solution.completePack(bagLoad, weight, value)
    res2 = solution.completePackDitto(bagLoad, weight, value)
    print(res1, res2)
