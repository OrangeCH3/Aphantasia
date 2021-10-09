#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.08 9:46
# @File     : 03-快乐数.py
# @Project  : AGTD


# 编写一个算法来判断一个数 n 是不是快乐数。

class Solution:

    def isHappy(self, n):

        def calculate_happy(num):
            sum_echo = 0
            while num:
                sum_echo += (num % 10) ** 2
                num = num // 10
            return sum_echo

        # 记录中间结果
        record = set()

        while True:
            n = calculate_happy(n)

            if n == 1:
                return True

            if n in record:
                return False
            else:
                record.add(n)


if __name__ == '__main__':

    # n = 19
    n = 33
    s = Solution()
    res = s.isHappy(n)
    print(res)
