#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.09 9:39
# @File     : 03-替换空格.py
# @Project  : AGTD


# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"

# 很多数组填充类的问题，都可以先预先给数组扩容带填充后的大小，然后在从后向前进行操作
# 1. 不用申请新数组
# 2. 从后向前填充元素，避免了从前先后填充元素要来的 每次添加元素都要将添加元素之后的所有元素向后移动


def replaceSpace(s):

    counter = s.count(' ')

    res = list(s)

    res.extend([' '] * counter * 2)

    old, new = len(s)-1, len(res)-1

    while old >= 0:
        if res[old] != ' ':
            res[new] = res[old]
            new -= 1
        else:
            res[new-2: new+1] = '%20'
            new -= 3
        old -= 1

    return ''.join(res)


def replaceSpaceDitto(s):
    s_list = s.split(' ')
    return '%20'.join(s_list)


if __name__ == '__main__':

    s = "We are happy."
    res = replaceSpace(s)
    res1 = replaceSpaceDitto(s)
    print(res,res1)
