#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.03 10:13
# @File     : 11-最后一块石头的重量.py
# @Project  : AGTD


class Solution(object):

    # 求背包最多能装多少
    def lastStoneWeight(self, stones):
        sum_weight = sum(stones)
        target = sum_weight // 2
        dp = [0] * 15001

        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

        return sum_weight - dp[target] - dp[target]


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    solution = Solution()
    res = solution.lastStoneWeight(stones)
    print(res)
