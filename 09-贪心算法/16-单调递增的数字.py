#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 16:56
# @File     : 16-单调递增的数字.py
# @Project  : AGTD


class Solution(object):

    def monotoneIncreasingDigits(self, n):

        a = list(str(n))

        for i in range(len(a)-1, 0, -1):  # 从右到左遍历

            if int(a[i]) < int(a[i-1]):
                a[i-1] = str(int(a[i-1])-1)
                a[i:] = '9' * (len(a) -i)  # i以后的位均置为9

        return int("".join(a))


if __name__ == '__main__':
    n = 33245
    solution = Solution()
    res = solution.monotoneIncreasingDigits(n)
    print(res)
