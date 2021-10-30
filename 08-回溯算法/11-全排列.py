#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.27 17:11
# @File     : 11-全排列.py
# @Project  : AGTD


# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。


class Solution(object):

    def permute(self, nums):

        res = []
        path = []
        used = []

        def backtrack(nums, used):
            if len(path) == len(nums):
                return res.append(path[:])
            for i in range(len(nums)):
                if nums[i] in used:
                    continue  # used里已经收录的元素，直接跳过
                path.append(nums[i])
                used.append(nums[i])
                backtrack(nums, used)
                used.pop()
                path.pop()

        backtrack(nums, used)
        return res

    # 优化：不用used数组
    def permuteDitto(self, nums):

        res = []
        path = []

        def backtrack(nums):
            if len(path) == len(nums):
                return res.append(path[:])
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums)
                path.pop()

        backtrack(nums)
        return res


if __name__ == '__main__':

    nums = [1, 2, 3]
    s = Solution()
    res = s.permute(nums)
    res1 = s.permuteDitto(nums)
    print(res)
    print(res1)
