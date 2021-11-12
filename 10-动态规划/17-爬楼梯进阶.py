#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.04 9:52
# @File     : 17-爬楼梯进阶.py
# @Project  : AGTD


# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 一步一个台阶，两个台阶，三个台阶，直到 m个台阶。
# 问有多少种不同的方法可以爬到楼顶呢？


class Solution(object):

    # 这是背包里求排列问题，即：1、2 步 和 2、1 步都是上三个台阶，但是这两种方法不一样！
    # 所以需将target放在外循环，将nums放在内循环。
    def climbStairs(self, n, m):
        dp = [0] * (n + 1)
        dp[0] = 1

        for j in range(n + 1):
            for i in range(1, m + 1):
                dp[j] += dp[j - i]

        return dp[-1]


if __name__ == '__main__':
    n = 7
    m = 3
    solution = Solution()
    res = solution.climbStairs(n, m)
    print(res)
