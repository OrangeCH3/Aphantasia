#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.26 21:06
# @File     : 05-组合总和.py
# @Project  : AGTD


# 给定一个数组 candidates 和一个目标数 target
# 找出 candidates 中所有可以使数字和为 target 的组合
# candidates 中的每个数字在每个组合中只能使用一次


class Solution(object):

    def combinationSum2(self, candidates, target):
        res = []
        path = []

        def backtrack(candidates, target, sum, start):
            if sum > target:
                return
            if sum == target:
                res.append(path[:])

            for i in range(start, len(candidates)):
                if sum + candidates[i] > target:
                    return
                if i > start and candidates[i] == candidates[i-1]:  # 要对同一树层使用过的元素进行跳过
                    continue

                sum += candidates[i]
                path.append(candidates[i])
                backtrack(candidates, target, sum, i + 1)  # i+1:每个数字在每个组合中只能使用一次
                sum -= candidates[i]  # 回溯
                path.pop()  # 回溯

        candidates = sorted(candidates)
        backtrack(candidates, target, 0, 0)
        return res


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    s = Solution()
    res = s.combinationSum2(candidates, target)
    print(res)
