#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.22 20:25
# @File     : 03-下一个更大元素.py
# @Project  : AGTD


class Solution(object):

    def nextGreaterElements(self, nums):
        n = len(nums)
        dp = [-1 for _ in range(n)]
        stack = []

        for i in range(n * 2):
            while len(stack) != 0 and nums[i % n] > nums[stack[-1]]:
                dp[stack[-1]] = nums[i % n]
                stack.pop()
            stack.append(i % n)

        return dp


if __name__ == '__main__':
    nums = [1, 2, 1, 4, 2]
    solution = Solution()
    res = solution.nextGreaterElements(nums)
    print(res)
