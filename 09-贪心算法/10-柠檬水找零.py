#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 9:35
# @File     : 10-柠檬水找零.py
# @Project  : AGTD


class Solution(object):

    def lemonadeChange(self, bills):

        five, ten, twenty = 0, 0, 0

        for bill in bills:

            if bill == 5:
                five += 1

            elif bill == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1

            else:
                if ten > 0 and five > 0:  # 贪心策略，优先使用ten完成找零
                    ten -= 1
                    five -= 1
                    twenty += 1
                elif five > 2:
                    five -= 3
                    twenty += 1
                else:
                    return False

        return True


if __name__ == '__main__':
    bills1 = [5, 5, 10]
    bills2 = [5, 5, 5, 10, 20]
    bills3 = [10, 10]
    bills4 = [5, 5, 10, 10, 20]
    solution = Solution()
    res1 = solution.lemonadeChange(bills1)
    res2 = solution.lemonadeChange(bills2)
    res3 = solution.lemonadeChange(bills3)
    res4 = solution.lemonadeChange(bills4)
    print(res1, res2, res3, res4)
