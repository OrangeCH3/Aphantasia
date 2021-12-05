#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.15 16:33
# @File     : 37-判断子序列.py
# @Project  : AGTD


class Solution(object):

    def isSubsequence(self, s, t):
        len1, len2 = len(s) + 1, len(t) + 1
        dp = [[0 for _ in range(len2)] for _ in range(len1)]

        for i in range(1, len1):
            for j in range(1, len2):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        if dp[-1][-1] == len1 - 1:
            return True, dp

        return False, dp


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
