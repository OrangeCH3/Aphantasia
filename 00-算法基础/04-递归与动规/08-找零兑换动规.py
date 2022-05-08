#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 10:46
# @File     : 08-找零兑换动规.py
# @Project  : AGTD


# 动态规划解决找零兑换
# 在生成最优解列表 dp 的同时，跟踪记录所选择的那个硬币币值形成 coinused 列表
# 在得到最后的解后，减去选择的硬币币值，回溯到表格之前的部分找零，就能逐步得到每一步所选择的硬币币值
def dpMC(pool, change):
    dp = [0] * (change + 1)
    coinused = [0] * (change + 1)
    for cent in range(1, change + 1):
        count = cent
        coinuse = 1
        for j in [c for c in pool if c <= cent]:
            if dp[cent - j] + 1 < count:
                count = dp[cent - j] + 1
                coinuse = j
        dp[cent] = count
        coinused[cent] = coinuse

    # 回溯
    coin = change
    coins = []
    while coin > 0:
        thiscoin = coinused[coin]
        coins.append(thiscoin)
        coin -= thiscoin

    return dp[-1], coins


if __name__ == '__main__':
    print(dpMC([1, 5, 10, 21, 25], 63)[0])
    print(dpMC([1, 5, 10, 21, 25], 63)[1])
