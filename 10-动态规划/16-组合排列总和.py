#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.04 9:42
# @File     : 16-组合排列总和.py
# @Project  : AGTD


# 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
# nums = [1, 2, 3] target = 4
# 所有可能的组合为： (1, 1, 1, 1) (1, 1, 2) (1, 2, 1) (1, 3) (2, 1, 1) (2, 2) (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。


class Solution(object):

    def combinationSum(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1

        # 求排列数就是外层for遍历背包，内层for循环遍历物品
        for j in range(target + 1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]

        return dp[-1]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    solution = Solution()
    res = solution.combinationSum(nums, target)
    print(res)
