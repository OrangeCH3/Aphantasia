#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 12:58
# @File     : 06-整数拆分.py
# @Project  : AGTD


class Solution(object):

    def integerBreak(self, n):
        dp = [0] * (n + 1)
        dp[:3] = [None, None, 1]

        for i in range(3, n + 1):
            for j in range(1, i - 1):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))

        return dp[n], dp


if __name__ == '__main__':
    n = 17
    solution = Solution()
    res = solution.integerBreak(n)
    print(res)
