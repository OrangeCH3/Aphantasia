#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.27 19:31
# @File     : 12-全排列.py
# @Project  : AGTD


# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。


class Solution(object):

    def permuteUnique(self, nums):

        res = []
        path = []
        used = [0] * len(nums)

        def backtrack(nums, used, path):
            if len(path) == len(nums):
                return res.append(path[:])
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtrack(nums, used, path)
                    path.pop()
                    used[i] = 0
        nums = sorted(nums)
        backtrack(nums, used, path)
        return res


if __name__ == '__main__':
    nums = [1, 1, 2]
    s = Solution()
    res = s.permuteUnique(nums)
    print(res)
