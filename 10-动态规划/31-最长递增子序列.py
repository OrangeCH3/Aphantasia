#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.09 15:12
# @File     : 31-最长递增子序列.py
# @Project  : AGTD


class Solution(object):

    def lengthOfLIS(self, nums):

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    nums2 = [3, 4]
    nums3 = [2]
    nums4 = [2, 1]
    solution = Solution()
    res1 = solution.lengthOfLIS(nums1)
    res2 = solution.lengthOfLIS(nums2)
    res3 = solution.lengthOfLIS(nums3)
    res4 = solution.lengthOfLIS(nums4)
    print(res1, res2, res3, res4)
