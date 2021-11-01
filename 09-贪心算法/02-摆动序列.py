#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.31 12:27
# @File     : 02-摆动序列.py
# @Project  : AGTD


class Solution(object):

    def wiggleMaxLength(self, nums):

        pre, cur, res = 0, 0, 1  # 题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度

        for i in range(len(nums) - 1):
            cur = nums[i + 1] - nums[i]
            if cur * pre <= 0 and cur != 0:
                res += 1
                pre = cur

        return res


if __name__ == '__main__':
    nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    solution = Solution()
    res = solution.wiggleMaxLength(nums)
    print(res)
