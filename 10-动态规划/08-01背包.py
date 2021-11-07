#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 13:36
# @File     : 08-01背包.py
# @Project  : AGTD


# 二维数组
class Solution(object):

    def bag01Problem(self, bagLoad, weight, value):
        """
        :param bagLoad: int
        :param weight: List[int]
        :param value: List[int]
        :return: int, List[List[int]]
        """
        row, col = len(weight), bagLoad + 1
        dp = [[0 for _ in range(col)] for _ in range(row)]
        res = 0

        # 初始化dp[][]
        for i in range(row):
            dp[i][0] = 0
        first_weight, first_value = weight[0], value[0]
        for j in range(1, col):
            if j >= first_weight:
                dp[0][j] = first_value

        # 更新dp数组: 先遍历物品, 再遍历背包
        for i in range(1, row):
            for j in range(1, col):
                if weight[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

                    if dp[i][j] > res:
                        res = dp[i][j]

        return res, dp


if __name__ == '__main__':
    bagLoad = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    solution = Solution()
    res = solution.bag01Problem(bagLoad, weight, value)
    print(res)
