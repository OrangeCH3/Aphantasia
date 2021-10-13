#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.09 9:21
# @File     : 02-跳步反转字符子串.py
# @Project  : AGTD


# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。


def reverseJumpStr(s, k):
    """
    1. 使用range(start, end, step)来确定需要调换的初始位置
    2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'
       字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
    3. 用切片整体替换，而不是一个个替换
    :param s: str
    :param k: int
    :return: str
    """

    def reverse_substr(text):
        left, right = 0, len(text) - 1
        while left < right:
            text[left], text[right] = text[right], text[left]
            left += 1
            right -= 1
        return text

    res = list(s)
    lenth = len(s)

    for point in range(0, lenth, 2*k):
        res[point: point+k] = reverse_substr(res[point: point+k])

    return ''.join(res)


if __name__ == '__main__':

    s = "abcdefghls"
    k = 2

    res = reverseJumpStr(s, k)
    print(res)
