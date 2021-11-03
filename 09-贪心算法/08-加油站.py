#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.31 14:59
# @File     : 08-加油站.py
# @Project  : AGTD


class Solution(object):

    def canCompleteCircuit(self, gas, cost):

        start, cursum, totalsum = 0, 0, 0

        for i in range(len(gas)):
            cursum += gas[i] - cost[i]
            totalsum += gas[i] - cost[i]
            if cursum < 0:
                cursum = 0
                start = i + 1

        if totalsum < 0:
            return -1
        return start


if __name__ == '__main__':
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    solution = Solution()
    res1 = solution.canCompleteCircuit(gas1, cost1)
    res2 = solution.canCompleteCircuit(gas2, cost2)
    print(res1, res2)
