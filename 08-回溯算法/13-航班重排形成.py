#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.30 12:06
# @File     : 13-航班重排形成.py
# @Project  : AGTD


import collections


class Solution(object):

    def findItinerary(self, tickets):

        tickets_dict = collections.defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])  # {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']}

        path = ["JFK"]

        def backtrack(start):
            if len(path) == len(tickets) + 1:
                return True
            tickets_dict[start].sort()

            for _ in tickets_dict[start]:
                end = tickets_dict[start].pop(0)
                path.append(end)
                if backtrack(end):
                    return True
                path.pop()
                tickets[start].append(end)

        backtrack("JFK")
        return path


if __name__ == '__main__':

    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

    s = Solution()
    res = s.findItinerary(tickets)
    print(res)
