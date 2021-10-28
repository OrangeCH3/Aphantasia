#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.26 20:46
# @File     : 04-组合总和.py
# @Project  : AGTD


# 给定一个无重复元素的数组 candidates 和一个目标数 target
# 找出 candidates 中所有可以使数字和为 target 的组合
# candidates 中的数字可以无限制重复被选取


class Solution(object):

    def combinationSum1(self, candidates, target):
        res = []
        path = []

        def backtrack(candidates, target, sum, start):

            if sum > target:
                return
            if sum == target:
                return res.append(path[:])

            for i in range(start, len(candidates)):
                if sum + candidates[i] > target:  # 如果 sum + candidates[i] > target 就终止遍历
                    return

                sum += candidates[i]
                path.append(candidates[i])
                backtrack(candidates, target, sum, i)  # start = i:表示可以重复读取当前的数
                sum -= candidates[i]
                path.pop()

        candidates = sorted(candidates)
        backtrack(candidates, target, 0, 0)
        return res


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8

    s = Solution()
    res = s.combinationSum1(candidates, target)
    print(res)
