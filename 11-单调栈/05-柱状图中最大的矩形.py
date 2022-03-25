#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.23 15:01
# @File     : 05-柱状图中最大的矩形.py
# @Project  : AGTD


class Solution(object):

    # 双指针法
    def largestRectangleArea(self, heights):
        n = len(heights)
        res = 0

        for i in range(n):
            left, right = i, i
            for _ in range(left, -1, -1):
                if heights[left] < heights[i]:
                    break
                left -= 1
            for _ in range(right, n):
                if heights[right] < heights[i]:
                    break
                right += 1

            width = right - left - 1
            height = heights[i]
            res = max(res, width * height)

        return res

    # 动态规划法
    def largestRectangleAreaDitto(self, heights):
        n = len(heights)
        # 两个DP数列储存的均是下标index
        min_left_index = [0] * n
        min_right_index = [0] * n
        res = 0

        min_left_index[0] = -1  # 初始化防止while死循环
        for i in range(1, n):
            tmp = i - 1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = min_left_index[tmp]
            min_left_index[i] = tmp
        min_right_index[n - 1] = n  # 初始化防止while死循环
        for i in range(n - 2, -1, -1):
            tmp = i + 1
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = min_right_index[tmp]
            min_right_index[i] = tmp

        for i in range(n):
            tmpres = heights[i] * (min_right_index[i] - min_left_index[i] - 1)
            res = max(res, tmpres)

        return res

    # 单调栈法
    def largestRectangleAreaDittoo(self, heights):
        n = len(heights)
        heights.insert(0, 0)  # padding
        heights.append(0)  # padding
        stack = [0]
        result = 0

        for i in range(1, n):
            while stack and heights[i] < heights[stack[-1]]:
                mid_height = heights[stack[-1]]
                stack.pop()
                if stack:
                    area = (i - stack[-1] - 1) * mid_height
                    result = max(area, result)
            stack.append(i)

        return result


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    solution = Solution()

    res0 = solution.largestRectangleArea(heights)
    print(res0)

    res1 = solution.largestRectangleAreaDitto(heights)
    print(res1)

    res2 = solution.largestRectangleAreaDittoo(heights)
    print(res2)
