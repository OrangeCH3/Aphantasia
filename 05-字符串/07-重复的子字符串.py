#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.14 9:07
# @File     : 07-重复的子字符串.py
# @Project  : AGTD


# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
# 给定的字符串只含有小写英文字母，并且长度不超过10000。


class Solution(object):

    def repeatedSubstringPattern(self, s):

        if len(s) == 0:
            return False

        next = [0] * len(s)
        self.getNext(next, s)
        print(next)

        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True

        return False

    def getNext(self, nxt, s):
        nxt[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt


if __name__ == '__main__':
    str1 = "abcabcabcabc"
    s = Solution()
    res = s.repeatedSubstringPattern(str1)
    print(res)
