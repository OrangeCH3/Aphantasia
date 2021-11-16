#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.05 12:44
# @File     : 21-多重背包.py
# @Project  : AGTD


class Solution(object):

    def multiPack(self, bagLoad, weight, value, nums):
        """
        :param bagLoad: int
        :param weight: List[int]
        :param value: List[int]
        :param nums: List[int]
        :return: int, List[int]
        """
        # 将物品展开数量为1，转化成0-1背包问题
        for i in range(len(nums)):
            while nums[i] > 1:
                weight.append(weight[i])
                value.append(value[i])
                nums[i] -= 1

        dp = [0] * (bagLoad + 1)
        for i in range(len(weight)):
            for j in range(bagLoad, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        print(" ".join(map(str, dp)))


if __name__ == '__main__':
    bagLoad = 10
    weight = [1, 3, 4]
    value = [15, 20, 30]
    nums = [2, 3, 2]
    solution = Solution()
    solution.multiPack(bagLoad, weight, value, nums)
