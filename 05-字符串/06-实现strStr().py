#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.13 15:15
# @File     : 06-实现strStr().py
# @Project  : AGTD


# 实现 strStr() 函数。
# 本题是KMP 经典题目


class Solution(object):

    def strStr(self, haystack, needle):
        a, b = len(needle), len(haystack)

        if a == 0:
            return 0

        next = self.getNext(a, needle)
        # print(next)
        p = 0
        for j in range(b):
            while p > 0 and needle[p] != haystack[j]:
                p = next[p-1]
            if needle[p] == haystack[j]:
                p += 1
            if p == a:
                return j-a+1

        return -1

    def getNext(self, a, needle):
        next = ['' for i in range(a)]
        k = 0
        next[0] = k
        for i in range(1, a):
            while k > 0 and needle[k] != needle[i]:
                k = next[k-1]
            if needle[k] == needle[i]:
                k += 1
            next[i] = k
        return next


if __name__ == '__main__':
    haystack = "aabaabaafa"
    needle = "abaaf"

    s = Solution()
    res = s.strStr(haystack, needle)
    print(res)
