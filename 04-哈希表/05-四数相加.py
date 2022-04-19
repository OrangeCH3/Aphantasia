#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.08 14:49
# @File     : 05-四数相加.py
# @Project  : AGTD


# 给定四个包含整数的数组列表 A , B , C , D
# 计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0

# 1. 首先定义一个unordered_map，key放a和b两数之和，value 放a和b两数之和出现的次数。
# 2. 遍历大A和大B数组，统计两个数组元素之和，和出现的次数，放到map中。
# 3. 定义int变量count，用来统计 a+b+c+d = 0 出现的次数。
# 4. 在遍历大C和大D数组，找到如果 0-(c+d) 在map中出现过的话，就用count把map中key对应的value也就是出现次数统计出来。
# 5. 最后返回统计值 count 就可以了

# dict()
class Solution(object):

    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :param nums3: List[int]
        :param nums4: List[int]
        :return: int
        """

        # use a dict to store the elements in nums1 and nums2 and their sum
        map_echo = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in map_echo:
                    map_echo[n1 + n2] += 1
                else:
                    map_echo[n1 + n2] = 1

        # if the -(a+b) exists in nums3 and nums4, we shall add the count
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = -(n3 + n4)
                if key in map_echo:
                    count += map_echo[key]

        return count


if __name__ == '__main1__':
    a = [1, 2]
    b = [-2, -1]
    c = [-1, 2]
    d = [0, 2]

    s = Solution()
    res = s.fourSumCount(a, b, c, d)
    print(res)

# -------分割线-------


# defaultdict()
from collections import defaultdict


class SolutionDitto(object):

    def fourSumCountDitto(self, nums1, nums2, nums3, nums4):

        # 当defaultdict里的key不存在但被查找时，返回的不是keyError而是一个默认值0
        map_ditto = defaultdict(int)

        for x1 in nums1:
            for x2 in nums2:
                map_ditto[x1 + x2] += 1

        count_ditto = 0
        for x3 in nums3:
            for x4 in nums4:
                key_ditto = -x3 - x4
                value = map_ditto[key_ditto]  # 若差值(key)不存在，则value返回0
                count_ditto += value

        return count_ditto


if __name__ == '__main__':
    a = [1, 2, 2]
    b = [-2, -1, 0]
    c = [-1, 2, -2]
    d = [0, 2, -1]

    s = SolutionDitto()
    res = s.fourSumCountDitto(a, b, c, d)
    print(res)
