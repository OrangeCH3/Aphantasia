#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.26 21:24
# @File     : 06-分割回文串.py
# @Project  : AGTD


class Solution(object):

    def partition(self, s):

        res = []
        path = []

        def backtrack(s, start):
            if start >= len(s):
                return res.append(path[:])

            for i in range(start, len(s)):
                p = s[start: i + 1]

                if p == p[::-1]:
                    path.append(p)
                else:
                    continue

                backtrack(s, i + 1)
                path.pop()

        backtrack(s, 0)
        return res


if __name__ == '__main__':
    str1 = "aab"
    s = Solution()
    res = s.partition(str1)
    print(res)
