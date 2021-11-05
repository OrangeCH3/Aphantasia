#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 12:22
# @File     : 04-不同路径.py
# @Project  : AGTD


class Solution(object):

    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):  # 先层(行)遍历
            for j in range(1, n):  # 后列遍历
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1], dp


if __name__ == '__main__':
    m, n = 7, 3
    solution = Solution()
    res = solution.uniquePaths(m, n)
    print(res)
