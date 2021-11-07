#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 14:04
# @File     : 09-01背包.py
# @Project  : AGTD


# 滚动数组
class Solution(object):

    def bag01ProblemDitto(self, bagLoad, weight, value):
        dp = [0] * (bagLoad + 1)

        for i in range(len(weight)):
            for j in range(bagLoad, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        return dp


if __name__ == '__main__':
    bagLoad = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    solution = Solution()
    res = solution.bag01ProblemDitto(bagLoad, weight, value)
    print(res)
