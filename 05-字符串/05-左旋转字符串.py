#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.13 15:03
# @File     : 05-左旋转字符串.py
# @Project  : AGTD


# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
# 请定义一个函数实现字符串左旋转操作的功能。
# 不能申请额外空间，只能在本串上操作。
# 输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。


# 1. 反转区间为前n的子串
# 2. 反转区间为n到末尾的子串
# 3. 反转整个字符串

class Solution(object):

    # 1. 使用切片的方法
    def reverseLeftWords(self, s, n):
        return s[n:] + s[0:n]

    # 2. 使用反转子字符串的方法
    def reverseLeftWordsDitto(self, s, n):
        def reverse_substr(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        tmp = list(s)
        end = len(tmp) - 1
        reverse_substr(tmp, 0, n - 1)
        reverse_substr(tmp, n, end)
        reverse_substr(tmp, 0, end)

        return ''.join(tmp)


if __name__ == '__main__':
    str1 = "slabcdefghj"
    n = 2

    s = Solution()
    res = s.reverseLeftWords(str1, n)
    res1 = s.reverseLeftWordsDitto(str1, n)
    print(res)
    print(res1)
