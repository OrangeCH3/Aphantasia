#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.26 9:43
# @File     : 01-组合问题.py
# @Project  : AGTD


# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。


class Solution(object):

    def combine(self, n, k):
        res = []
        path = []

        def backtrack(n, k, start):
            if len(path) == k:
                res.append(path[:])
                return
            # for i in range(start, n+1):  # 未做剪枝优化，效率较低
            for i in range(start, n-(k-len(path))+2):  # 剪枝优化
                path.append(i)  # 处理节点
                backtrack(n, k, i+1)  # 递归
                path.pop()  # 回溯，撤销处理的节点

        backtrack(n, k, 1)
        return res


if __name__ == '__main__':

    n, k = 4, 2
    s = Solution()
    res = s.combine(n, k)
    print(res)
