#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 11:04
# @File     : 15-合并区间.py
# @Project  : AGTD


class Solution(object):

    def merge(self, intervals):

        if len(intervals) == 0:
            return intervals

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):

            last = result[-1]

            if last[1] > intervals[i][0]:
                result[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                result.append(intervals[i])

        return result


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    solution = Solution()
    res = solution.merge(intervals)
    print(res)
