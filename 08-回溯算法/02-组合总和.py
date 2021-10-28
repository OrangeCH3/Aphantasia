#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.26 9:56
# @File     : 02-组合总和.py
# @Project  : AGTD


# 找出所有相加之和为 n 的 k 个数的组合。
# 组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

# 示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]
# 示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):

    def combinationSum3(self, k, n):

        res = []
        path = []

        def findallPath(k, n, sum, start):
            if sum > n:  # 剪枝操作
                return
            if sum == n and len(path) == k:
                return res.append(path[:])

            for i in range(start, 9-(k-len(path))+2):  # 剪枝操作
                path.append(i)
                sum += i
                findallPath(k, n, sum, i+1)
                path.pop()
                sum -= i

        findallPath(k, n, 0, 1)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.combinationSum3(3, 9)
    print(res)

