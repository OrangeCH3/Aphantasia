#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 13:15
# @File     : 07-不同的二叉搜索树.py
# @Project  : AGTD


class Solution(object):

    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[:2] = [1, 1]  # n为0时可以当成是一个空树，计数为1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1], dp


if __name__ == '__main__':
    n = 7
    solution = Solution()
    res = solution.numTrees(n)
    print(res)
