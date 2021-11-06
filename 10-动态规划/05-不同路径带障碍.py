#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 12:31
# @File     : 05-不同路径带障碍.py
# @Project  : AGTD


class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        # 构造一个DP table
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        # 如果第一个格子就是障碍，return 0
        if dp[0][0] == 0:
            return 0

        for i in range(1, col):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i - 1]

        for j in range(1, row):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = dp[j - 1][0]

        # print(dp)

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1], dp


if __name__ == '__main__':
    obstacleGrid = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    solution = Solution()
    res = solution.uniquePathsWithObstacles(obstacleGrid)
    print(res)
