#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.27 10:48
# @File     : 09-子集问题.py
# @Project  : AGTD


# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。


class Soultion(object):

    def subsetsWithDup(self, nums):

        res = []
        path = []

        def backtrack(nums, start):

            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()

        nums = sorted(nums)
        backtrack(nums, 0)
        return res


if __name__ == '__main__':

    nums = [1, 2, 2]
    s = Soultion()
    res = s.subsetsWithDup(nums)
    print(res)
