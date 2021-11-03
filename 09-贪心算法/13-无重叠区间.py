#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 10:18
# @File     : 13-无重叠区间.py
# @Project  : AGTD


class Solution(object):

    def eraseOverlapIntervals(self, intervals):

        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[1])

        count = 1  # 记录非交叉区间的个数
        end = intervals[0][1]  # 记录区间分割点

        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                count += 1
                end = intervals[i][1]

        return len(intervals) - count


if __name__ == '__main__':
    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    intervals2 = [[1, 2], [1, 2], [1, 2]]
    solution = Solution()
    res1 = solution.eraseOverlapIntervals(intervals1)
    res2 = solution.eraseOverlapIntervals(intervals2)
    print(res1, res2)
