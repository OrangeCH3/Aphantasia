#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.09 16:51
# @File     : 34-最长公共子序列.py
# @Project  : AGTD


class Solution(object):

    def longestCommonSubsequence(self, text1, text2):
        len1, len2 = len(text1) + 1, len(text2) + 1
        dp = [[0 for _ in range(len1)] for _ in range(len2)]

        for i in range(1, len2):
            for j in range(1, len1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    solution = Solution()
    res = solution.longestCommonSubsequence(text1, text2)
    print(res)
