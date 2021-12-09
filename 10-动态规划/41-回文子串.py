#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.17 15:04
# @File     : 41-回文子串.py
# @Project  : AGTD


class Solution(object):

    # 动态规划法
    def countSubstrings(self, s):
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]
        result = 0

        # 遍历顺序按照从下到上，从左到右，且只填充矩阵右上三角部分
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # if s[j] == s[i]:
                #     if j - i <= 1:
                #         result += 1
                #         dp[i][j] = True
                #     elif dp[i + 1][j - 1]:
                #         result += 1
                #         dp[i][j] = True
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    result += 1
                    dp[i][j] = True

        return result

    # 双指针法
    def countSubstringsDitto(self, s):
        lenth = len(s)
        result = 0

        def extend(s, i, j, n):
            res = 0
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                res += 1
            return res

        for i in range(lenth):
            result += extend(s, i, i, lenth)  # 以i为中心
            result += extend(s, i, i + 1, lenth)  # 以i和i+1为中心

        return result


if __name__ == '__main__':
    s = "aaaba"
    solution = Solution()
    res = solution.countSubstrings(s)
    res1 = solution.countSubstringsDitto(s)
    print(res)
    print(res1)
