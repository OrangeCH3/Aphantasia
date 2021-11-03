#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 9:58
# @File     : 12-用最少数量的箭引爆气球.py
# @Project  : AGTD


class Solution(object):

    def findMinArrowShots(self, points):

        if len(points) == 0:
            return 0

        points.sort(key=lambda x: x[0])

        result = 1

        for i in range(1, len(points)):

            if points[i][0] > points[i - 1][1]:  # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])  # 更新重叠气球最小右边界

        return result


if __name__ == '__main__':
    points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
    points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    solution = Solution()
    res1 = solution.findMinArrowShots(points1)
    res2 = solution.findMinArrowShots(points2)
    print(res1, res2)
