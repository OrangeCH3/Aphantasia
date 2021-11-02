#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.31 13:50
# @File     : 05-跳跃游戏.py
# @Project  : AGTD


class Solution(object):

    def canJump(self, nums):
        if len(nums) == 1:
            return True

        cover = 0
        i = 0

        # python不支持动态修改for循环中变量,使用while循环代替
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1:
                return True
            i += 1

        return False


if __name__ == '__main__':
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]
    solution = Solution()
    res1 = solution.canJump(nums1)
    res2 = solution.canJump(nums2)
    print(res1, res2)
