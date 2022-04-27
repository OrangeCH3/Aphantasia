#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 10:56
# @File     : 14-划分字母区间.py
# @Project  : AGTD


class Solution(object):

    def partitionLabels(self, s):

        from collections import defaultdict

        record = defaultdict(int)

        for i in range(len(s)):
            record[s[i]] = i

        res = []
        l, r = 0, 0

        for j in range(len(s)):
            r = max(r, record[s[j]])

            if j == r:
                res.append(r - l + 1)
                l = r + 1

        return res


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    solution = Solution()
    res = solution.partitionLabels(s)
    print(res)
