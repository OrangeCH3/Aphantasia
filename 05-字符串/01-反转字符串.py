#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.09 9:05
# @File     : 01-反转字符串.py
# @Project  : AGTD


# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。


def reverseStr(s):
    """
     Do not return anything, modify s in-place instead.
    :param s: List[str]
    :return: None
    """

    left, right = 0, len(s) - 1

    # for i in range(right // 2):
    # 下方的循环条件更优越，且写法通俗易懂
    while left < right:

        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    # return s


if __name__ == '__main__':

    s = ["h", "e", "l", "l", "o"]
    reverseStr(s)
    print(s)


