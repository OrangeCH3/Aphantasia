#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.09 15:12
# @File     : 31-最长递增子序列.py
# @Project  : AGTD


class Solution(object):

    def lengthOfLIS(self, nums):
        n = len(nums)

        if n == 0:
            return 0

        dp = [1] * n
        result = 1

        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])

        return result


if __name__ == '__main__':
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    nums2 = []
    nums3 = [2]
    nums4 = [2, 1]
    solution = Solution()
    res1 = solution.lengthOfLIS(nums1)
    res2 = solution.lengthOfLIS(nums2)
    res3 = solution.lengthOfLIS(nums3)
    res4 = solution.lengthOfLIS(nums4)
    print(res1, res2, res3, res4)
