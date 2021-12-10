#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.17 15:17
# @File     : 42-最长回文子序列.py
# @Project  : AGTD


class Solution(object):

    def longestPalindromeSubseq(self, s):
        n = len(s)

        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1], dp


if __name__ == '__main__':
    s = "bbbab"
    solution = Solution()
    res = solution.longestPalindromeSubseq(s)
    print(res[0])
    print(res[1])
