#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.15 15:12
# @File     : 07-前K个高频元素.py
# @Project  : AGTD


# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。


import heapq
from collections import defaultdict


class Solution(object):

    def topKFrequent(self, nums, k):

        # 统计元素出现频率
        value_freque = defaultdict(int)

        for i in range(len(nums)):
            value_freque[nums[i]] += 1
        print(value_freque)

        # 定义一个小顶堆
        priority_queue = []

        for value, freq in value_freque.items():
            heapq.heappush(priority_queue, (freq, value))
            if len(priority_queue) > k:
                heapq.heappop(priority_queue)  # 从堆中弹出最小的元素
        print(priority_queue)

        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(priority_queue)[1]
        return result

    def topKFrequentDitto(self, nums, k):
        val_freq = defaultdict(int)

        for val in nums:
            val_freq[val] += 1

        val_freq_sort = sorted(val_freq.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(val_freq_sort[i][0])
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    s = Solution()
    res = s.topKFrequent(nums, k)
    print(res)
    res1 = s.topKFrequentDitto(nums, k)
    print(res1)
