#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.27 16:06
# @File     : 10-递增子序列.py
# @Project  : AGTD


class Solution(object):

    def findSubsequences(self, nums):

        res = []
        path = []

        def backtrack(nums, start):

            repeat = []  # 这里使用数组来进行去重操作
            if len(path) >= 2:
                res.append(path[:])

            for i in range(start, len(nums)):
                if nums[i] in repeat:
                    continue
                if len(path) >= 1:
                    if nums[i] < path[-1]:
                        continue
                repeat.append(nums[i])
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()

        backtrack(nums, 0)
        return res


if __name__ == '__main__':

    nums = [4, 7, 6, 7]
    s = Solution()
    res = s.findSubsequences(nums)
    print(res)
