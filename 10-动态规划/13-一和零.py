#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.03 12:11
# @File     : 13-一和零.py
# @Project  : AGTD


# 二维0-1背包
class Solution(object):

    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 遍历物品
        for str in strs:
            ones = str.count('1')
            zeros = str.count('0')

            # 遍历背包容量且从后向前遍历
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]


if __name__ == '__main__':
    strs1 = ["10", "0001", "111001", "1", "0"]
    m1 = 5
    n1 = 3

    strs2 = ["10", "0", "1"]
    m2 = 1
    n2 = 1

    solution = Solution()
    res1 = solution.findMaxForm(strs1, m1, n1)
    res2 = solution.findMaxForm(strs2, m2, n2)

    print(res1)
    print(res2)
