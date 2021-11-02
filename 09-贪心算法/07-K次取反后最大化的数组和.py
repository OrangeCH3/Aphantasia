#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.31 14:28
# @File     : 07-K次取反后最大化的数组和.py
# @Project  : AGTD


class Solution(object):

    def largestSumAfterKNegations(self, nums, k):
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
        if k > 0:
            nums[-1] *= (-1)**k

        return sum(nums)


if __name__ == '__main__':
    nums1 = [2, -3, -1, 5, -4]
    k1 = 2

    nums2 = [3, -1, 0, 2]
    k2 = 3

    solution = Solution()
    res1 =solution.largestSumAfterKNegations(nums1, k1)
    res2 =solution.largestSumAfterKNegations(nums2, k2)
    print(res1, res2)
