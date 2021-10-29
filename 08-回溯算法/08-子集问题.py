#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.27 10:41
# @File     : 08-子集问题.py
# @Project  : AGTD


# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。


class Solution(object):

    def subsets(self, nums):
        res = []
        path = []

        def backtrack(nums, start):
            res.append(path[:])  # 深复制，防止添加过的路径列表发生改变

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()

        backtrack(nums, 0)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    res = s.subsets(nums)
    print(res)


