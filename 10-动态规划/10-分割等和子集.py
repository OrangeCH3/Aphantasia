#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 17:21
# @File     : 10-分割等和子集.py
# @Project  : AGTD


class Solution(object):

    # 求背包是否正好装满
    def canPartition(self, nums):
        target = sum(nums)

        if target % 2 == 1:
            return False

        target //= 2
        dp = [0] * 10001

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        return target == dp[target]  # 集合中的子集总和正好可以凑成总和i


if __name__ == '__main__':
    nums1 = [1, 5, 11, 5]
    nums2 = [1, 2, 3, 5]
    solution = Solution()
    res1 = solution.canPartition(nums1)
    res2 = solution.canPartition(nums2)
    print(res1, res2)
