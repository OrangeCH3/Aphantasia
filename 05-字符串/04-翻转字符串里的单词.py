#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.10 12:00
# @File     : 04-翻转字符串里的单词.py
# @Project  : AGTD


# 给定一个字符串，逐个翻转字符串中的每个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

class Solution(object):

    # 1. 去除多余的空格
    def trim_spaces(self, s):
        n = len(s)
        left, right = 0, n-1

        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        tmp = []
        while left <= right:  # 消除单词中间多余的空格
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':  # 若读取到空格，列表中最后一个元素不为空格，则添加
                tmp.append(s[left])
            left += 1
        return tmp

    # 2. 翻转整个字符数组
    def reverse_string(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None

    # 3. 翻转每个单词
    def reverse_each_word(self, nums):
        # 双指针法
        start, end = 0, 0
        n = len(nums)

        while start < n:
            while end < n and nums[end] != ' ':
                end += 1
            self.reverse_string(nums, start, end-1)
            start = end + 1
            end += 1
        return None


if __name__ == '__main__':

    str1 = ' the  sky is blue   '

    s = Solution()
    s_trim = s.trim_spaces(str1)
    s.reverse_string(s_trim, 0, len(s_trim)-1)
    s.reverse_each_word(s_trim)

    s_res = ''.join(s_trim)
    print(s_res)
