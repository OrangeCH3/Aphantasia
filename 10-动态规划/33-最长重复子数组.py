#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.09 16:09
# @File     : 33-最长重复子数组.py
# @Project  : AGTD


# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。


import numpy as np


class Solution(object):

    def findLength(self, A, B):

        row = len(A) + 1
        col = len(B) + 1

        # dp = [[0] * col] * row  # 行列均为浅拷贝，每一行的改变都会改变其他行
        # dp = [[0 for _ in range(col)] for _ in range(row)]  # 行列均为深拷贝

        # 行浅拷贝，列深拷贝，效果与行列均为深拷贝一致，每一行数据改变不会影响其他行
        dp = [[0] * col for _ in range(row)]
        result = 0

        for i in range(1, row):
            for j in range(1, col):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                result = max(result, dp[i][j])

        # return result, dp
        return np.max(dp), dp

    # 滚动数组动态规划，省空间
    def findLengthDitto(self, A, B):
        row = len(A) + 1
        col = len(B) + 1

        dp = [0]*col
        result = 0

        for i in range(1, row):
            for j in range(col-1, 0, -1):  # 从后向前遍历，这样避免数据覆盖
                if A[i-1] == B[j-1]:
                    dp[j] = dp[j-1]+1
                else:
                    dp[j] = 0
                result = max(result, dp[j])

        return result, dp


if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    solution = Solution()
    res = solution.findLength(A, B)
    print(res[0])
    print(res[1])
    res1 = solution.findLengthDitto(A, B)
    print(res1[0])
    print(res1[1])
