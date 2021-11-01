#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.30 13:21
# @File     : 01-分发饼干.py
# @Project  : AGTD


class Solution(object):
    # 可以使用贪心策略，先将饼干数组和小孩数组排序。
    # 然后从后向前遍历小孩数组，用大饼干优先满足胃口大的，并统计满足小孩数量。
    def findContentChildren(self, g, s):

        g.sort()
        s.sort()
        start, count = len(s)-1, 0

        for index in range(len(g)-1, -1, -1):
            if start >= 0 and g[index] <= s[start]:
                start -= 1
                count += 1
        return count


if __name__ == '__main__':
    g = [1, 2, 7, 10]
    s = [1, 3, 5, 9]
    solution = Solution()
    res = solution.findContentChildren(g, s)
    print(res)
