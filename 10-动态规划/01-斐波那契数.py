#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.02 9:41
# @File     : 01-斐波那契数.py
# @Project  : AGTD


class Soluiton(object):

    # 1. 动态规划法
    def fib(self, n):

        if n < 2:
            return n

        dp = [0, 1]
        a, b, c = 0, 1, 0

        for i in range(n - 1):
            c = a + b
            dp.append(c)
            a, b = b, c

        return c, dp

    # 2. 递归法
    def fibDitto(self, n):
        if n < 2:
            return n
        return self.fibDitto(n - 1) + self.fibDitto(n - 2)


if __name__ == '__main__':
    n = 10
    soluiton = Soluiton()
    res1 = soluiton.fib(n)
    res2 = soluiton.fibDitto(n)
    print("使用动态规划法：当n为{0}时，F(n)为{1}，对应的dp[]数组为：{2}".format(n, res1[0], res1[1]))
    print("使用递归法：当n为{0}时，F(n)为{1}".format(n, res2))
