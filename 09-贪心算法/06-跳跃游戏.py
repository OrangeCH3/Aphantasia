#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.31 14:15
# @File     : 06-跳跃游戏.py
# @Project  : AGTD


class Solution(object):

    def jumpMinSteps(self, nums):
        if len(nums) == 1:
            return 0

        result, curDistance, nextDistance = 0, 0, 0
        for i in range(len(nums)):
            nextDistance = max(nums[i] + i, nextDistance)
            if i == curDistance:
                if curDistance < len(nums) - 1:
                    result += 1
                    curDistance = nextDistance
                    if nextDistance >= len(nums) - 1:
                        break
        return result


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    solution = Solution()
    res = solution.jumpMinSteps(nums)
    print(res)
