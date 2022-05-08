#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.23 10:09
# @File     : 04-接雨水.py
# @Project  : AGTD


class Solution(object):

    # 双指针法(会超时)
    def trap(self, height):
        n = len(height)
        res = 0

        for i in range(n):
            if i == 0 or i == n - 1:
                continue

            lHeight = height[i - 1]
            rHeight = height[i + 1]
            for j in range(i - 1):
                if height[j] > lHeight:
                    lHeight = height[j]
            for k in range(i + 2, n):
                if height[k] > rHeight:
                    rHeight = height[k]

            tmpres = min(lHeight, rHeight) - height[i]
            if tmpres > 0:
                res += tmpres

        return res

    # 动态规划法
    def trapDitto(self, height):
        n = len(height)
        lHeight, rHeight = [0] * n, [0] * n

        lHeight[0] = height[0]
        for i in range(1, n):
            lHeight[i] = max(lHeight[i - 1], height[i])
        rHeight[-1] = height[-1]
        for j in range(n - 2, -1, -1):
            rHeight[j] = max(rHeight[j + 1], height[j])

        res = 0
        for k in range(n):
            tmpres = min(lHeight[k], rHeight[k]) - height[k]
            res += tmpres

        return res

    # 单调栈法
    def trapDittoo(self, height):
        n = len(height)
        stack = [0]
        res = 0

        for i in range(1, n):
            while stack and height[i] > height[stack[-1]]:
                midHeight = stack.pop()
                if stack:
                    h = min(height[stack[-1]], height[i]) - height[midHeight]
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)

        return res


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()

    res1 = solution.trap(height)
    print(res1)

    res2 = solution.trapDitto(height)
    print(res2)

    res3 = solution.trapDittoo(height)
    print(res3)
