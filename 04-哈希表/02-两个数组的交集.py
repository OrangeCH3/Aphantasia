#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.07 16:43
# @File     : 02-两个数组的交集.py
# @Project  : AGTD


# 给定两个数组，编写一个函数来计算它们的交集。


class Solution:

    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    nums1 = [1, 2, 3, 2]
    nums2 = [1, 4, 3, 2]
    s = Solution()
    res = s.intersection(nums1, nums2)
    print(res)
