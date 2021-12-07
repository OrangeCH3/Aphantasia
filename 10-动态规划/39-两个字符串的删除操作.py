#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.16 16:10
# @File     : 39-两个字符串的删除操作.py
# @Project  : AGTD


class Solution(object):

    def minDistance(self, word1, word2):
        len1, len2 = len(word1) + 1, len(word2) + 1

        dp = [[0 for _ in range(len2)] for _ in range(len1)]
        for i in range(len1):
            dp[i][0] = i
        for j in range(len2):
            dp[0][j] = j

        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 2)

        return dp[-1][-1], dp


if __name__ == '__main__':
    word1 = "sea"
    word2 = "eat"
    solution = Solution()
    res = solution.minDistance(word1, word2)
    print(res[0])
    print(res[1])
