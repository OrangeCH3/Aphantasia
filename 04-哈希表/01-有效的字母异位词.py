#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.07 16:24
# @File     : 01-有效的字母异位词.py
# @Project  : AGTD


# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。


# 1.数组形式
def is_anagram(s, t):
    record = [0] * 26

    for i in range(len(s)):
        record[ord(s[i]) - ord('a')] += 1

    print(record)

    for j in range(len(t)):
        record[ord(t[j]) - ord("a")] -= 1
    print(record)

    for k in range(26):
        if record[k] != 0:
            return False

    return True


if __name__ == '__main1__':
    s = "anagram"
    t = "nagaram"
    res = is_anagram(s, t)
    print(res)

# -------分割线-------


from collections import defaultdict


# 字典形式
def is_anagram2(s, t):
    s_dict = defaultdict(int)
    t_dict = defaultdict(int)

    for x in s:
        s_dict[x] += 1
    print(s_dict)

    for x in t:
        t_dict[x] += 1
    print(s_dict)

    return s_dict == t_dict


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    res = is_anagram2(s, t)
    print(res)
