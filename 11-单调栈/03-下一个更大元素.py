#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.22 20:25
# @File     : 03-下一个更大元素.py
# @Project  : AGTD


class Solution(object):

    def nextGreaterElements(self, nums):

        n = len(nums)
        res = [-1] * n
        stack = [0]

        for i in range(1, n * 2):
            if nums[i % n] <= nums[stack[-1]]:
                stack.append(i % n)
            else:
                while len(stack) != 0 and nums[i % n] > nums[stack[-1]]:
                    res[stack[-1]] = nums[i % n]
                    stack.pop()
                stack.append(i % n)

        return res


if __name__ == '__main__':
    nums = [1, 2, 1, 4, 2]
    solution = Solution()
    res = solution.nextGreaterElements(nums)
    print(res)
