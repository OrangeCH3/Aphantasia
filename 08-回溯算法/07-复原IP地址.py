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

        def bt(s, start):
            if len(path) == 4 and start == len(s):
                return res.append('.'.join(path[:]))

            for i in range(start, min(start + 4, len(s))):
                tmp = s[start:i + 1]
                if not 0 <= int(tmp) <= 255:
                    continue
                if tmp != '0' and tmp.lstrip('0') != tmp:
                    continue

                path.append(tmp)
                bt(s, i + 1)
                path.pop()

        bt(s, 0)
        return res


if __name__ == '__main__':
    str1 = "101023"
    s = Solution()
    res = s.restoreIpAddresses(str1)
    print(res)
