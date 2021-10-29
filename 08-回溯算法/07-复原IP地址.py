#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.27 10:20
# @File     : 07-复原IP地址.py
# @Project  : AGTD


class Solution(object):

    def restoreIpAddresses(self, s):

        res = []
        path = []

        def backtrack(path, start):
            if len(path) == 4 and start == len(s):
                return res.append(".".join(path[:]))

            for i in range(start+1, min(start+4, len(s)+1)):  # 剪枝
                string = s[start:i]
                if not 0 <= int(string) <= 255:
                    continue
                if string != "0" and string.lstrip("0") != string:
                    continue

                path.append(string)
                backtrack(path, i)
                path.pop()

        backtrack(path, 0)
        return res


if __name__ == '__main__':
    str1 = "101023"
    s = Solution()
    res = s.restoreIpAddresses(str1)
    print(res)
