#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.08 15:09
# @File     : 06-赎金信.py
# @Project  : AGTD


# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
# 判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
# 如果可以构成，返回 true ；否则返回 false。

from collections import defaultdict
from collections import Counter

class Solution(object):

    # 使用数组作为哈希表
    def can_construct1(self, ransom, magazine):
        """
        :param ransom: str
        :param magazine: str
        :return: bool
        """

        records = [0] * 26

        for x in magazine:
            records[ord(x) - ord('a')] += 1

        for y in ransom:
            if records[ord(y) - ord('a')] == 0:
                return False
            else:
                records[ord(y) - ord('a')] -= 1

        return True

    # 使用defaultdict()
    def can_construct2(self, ransom, magazine):

        map_echo = defaultdict(int)

        for x in magazine:
            map_echo[x] += 1

        for y in ransom:
            value = map_echo[y]
            if value == 0:
                return False
            else:
                map_echo[y] -= 1

        return True

    # 使用dict()
    def can_construct3(self, ransom, magazine):

        # use a dict to store the number of letter occurance in ransomNote
        hashmap = dict()
        for s in ransom:
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1

        # check if the letter we need can be found in magazine
        for l in magazine:
            if l in hashmap:
                hashmap[l] -= 1

        for key in hashmap:
            if hashmap[key] > 0:
                return False

        return True

    # 使用Counter()
    def can_construct4(self, ransom, magazine):

        c1 = Counter(ransom)
        c2 = Counter(magazine)
        x = c1 - c2
        # print(x.elements())

        # x只保留值大于0的符号，当c1里面的符号个数小于c2时，不会被保留
        # 所以x只保留下了，magazine不能表达的

        if len(x) == 0:
            return True
        else:
            return False


if __name__ == '__main__':

    ransom = "abcdefg"
    magazine = "abcdefgg"

    s = Solution()
    res1 = s.can_construct1(ransom, magazine)
    res2 = s.can_construct2(ransom, magazine)
    res3 = s.can_construct3(ransom, magazine)
    res4 = s.can_construct4(ransom, magazine)
    print(res1, res2, res3, res4)
