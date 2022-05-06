#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.15 16:33
# @File     : 37-判断子序列.py
# @Project  : AGTD


class Solution(object):

    def isSubsequence(self, s, t):

        row = len(s) + 1
        col = len(t) + 1

        dp = [[0] * col for _ in range(row)]

        for i in range(1, row):
            for j in range(1, col):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1] == len(s), dp


if __name__ == '__main__':
    s1 = "abc"
    t1 = "ahbgdc"
    s2 = "axc"
    t2 = "ahbgdc"
    solution = Solution()
    res1 = solution.isSubsequence(s1, t1)
    res2 = solution.isSubsequence(s2, t2)
    print(res1[0], res1[1])
    print(res2[0], res2[1])
