#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 9:52
# @File     : 11-根据身高重建队列.py
# @Project  : AGTD


class Solution(object):

    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))

        que = []

        for p in people:
            que.insert(p[1], p)

        return que


if __name__ == '__main__':
    people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    solution = Solution()
    res = solution.reconstructQueue(people)
    print(res)
