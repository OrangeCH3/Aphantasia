#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 10:06
# @File     : 07-找零兑换递归.py
# @Project  : AGTD


import time


# 递归解决找零兑换
# 中间结果记录 goodResults 可以很好解决找零兑换问题
# 这种方法还不能称为动态规划，而是叫做“Memoization（记忆化/函数值缓存）”的技术提高了递归解法的性能
def recMC(pool, change, goodResults):
    minCount = change
    if change in pool:  # 递归基本结束条件
        goodResults[change] = 1  # 记录最优解
        return 1
    elif goodResults[change] > 0:
        return goodResults[change]  # 查表成功，直接用最优解，消除重复运算
    else:
        for i in [c for c in pool if c <= change]:
            numCount = 1 + recMC(pool, change - i, goodResults)
            if numCount < minCount:
                minCount = numCount
                goodResults[change] = minCount  # 找到最优解，记录到表中

    return minCount


if __name__ == '__main__':
    timeBegin = time.perf_counter()
    print(recMC([1, 5, 10, 25], 63, [0] * 64))
    timeEnd = time.perf_counter()
    timeUse = round(timeEnd - timeBegin, 2)
    print(f"计算recMC([1, 5, 10, 25], 63)总共用时：{timeUse} S")
