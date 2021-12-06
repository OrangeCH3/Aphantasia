#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.16 15:52
# @File     : 38-不同的子序列.py
# @Project  : AGTD


class Solution(object):

    def numDistinct(self, s, t):
        len1, len2 = len(s) + 1, len(t) + 1

        dp = [[0 for _ in range(len2)] for _ in range(len1)]

        for i in range(len1):
            dp[i][0] = 1
        for j in range(1, len2):
            dp[0][j] = 0

        for i in range(1, len1):
            for j in range(1, len2):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1], dp

    # 省空间
    def numDistinctDitto(self,s,t):
        len1, len2 = len(s) + 1, len(t) + 1

        dp=[0 for _ in range(len2)]
        dp[0] = 1

        for i in range(1, len1):

            prev = dp[:]  # 深拷贝

            for j in range(1, len2):
                if s[i - 1] == t[j - 1]:
                    dp[j] = prev[j - 1] + prev[j]
                else:
                    dp[j] = prev[j]

        return dp[-1], dp


if __name__ == '__main__':
    s = "babgbag"
    t = "bag"
    solution = Solution()
    res = solution.numDistinct(s, t)
    print(res[0])
    print(res[1])
    res1 = solution.numDistinctDitto(s,t)
    print(res1[0])
    print(res1[1])
