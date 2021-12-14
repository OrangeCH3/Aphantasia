#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.18 10:25
# @File     : 02-下一个更大元素.py
# @Project  : AGTD


class Solution(object):

    def nextGreaterElement(self, nums1, nums2):
        n = len(nums1)
        result = [-1] * n
        stack = [0]

        for i in range(1, n):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        result[index] = nums2[i]
                    stack.pop()
                stack.append(i)

        return result


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    solution = Solution()
    res = solution.nextGreaterElement(nums1, nums2)
    print(res)
