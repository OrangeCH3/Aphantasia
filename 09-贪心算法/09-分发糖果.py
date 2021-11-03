#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.31 16:13
# @File     : 09-分发糖果.py
# @Project  : AGTD


class Solution(object):

    def candy(self, ratings):

        candyVec = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candyVec[i] = candyVec[i - 1] + 1

        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candyVec[j] = max(candyVec[j], candyVec[j + 1] + 1)

        return candyVec, sum(candyVec)


if __name__ == '__main__':
    ratings = [1, 2, 2, 5, 4, 3, 2]
    solution = Solution()
    res = solution.candy(ratings)
    print("具体分发糖果方案为: {0}\n总共需要准备{1}个糖果!".format(res[0], res[1]))
