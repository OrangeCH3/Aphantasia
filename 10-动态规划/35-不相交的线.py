#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.15 16:14
# @File     : 35-不相交的线.py
# @Project  : AGTD


class Solution(object):

    def maxUncrossedLines(self, A, B):
        len1, len2 = len(A) + 1, len(B) + 1
        dp = [[0 for _ in range(len2)] for _ in range(len1)]

        for i in range(1, len1):
            for j in range(1, len2):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    A = [2, 5, 1, 2, 5]
    B = [10, 5, 2, 1, 5, 2]
    solution = Solution()
    res = solution.maxUncrossedLines(A, B)
    print(res)
