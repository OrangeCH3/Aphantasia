#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 9:41
# @File     : 01-每日温度.py
# @Project  : AGTD


class Solution(object):

    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0 for _ in range(n)]
        stack = [0]

        for i in range(1, n):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)

        return result


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    res = solution.dailyTemperatures(temperatures)
    print(res)
