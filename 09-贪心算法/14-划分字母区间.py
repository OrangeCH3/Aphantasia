#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 10:56
# @File     : 14-划分字母区间.py
# @Project  : AGTD


class Solution(object):

    def partitionLabels(self, s):

        records = [0] * 26
        for i in range(len(s)):
            records[ord(s[i]) - ord('a')] = i  # 遍历所有字母的最远边界索引

        result = []
        left, right = 0, 0

        for j in range(len(s)):
            right = max(right, records[ord(s[j]) - ord('a')])

            if j == right:
                result.append(right - left + 1)
                left = j + 1

        return result


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    solution = Solution()
    res = solution.partitionLabels(s)
    print(res)
