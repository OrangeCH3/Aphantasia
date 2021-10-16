#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.14 14:43
# @File     : 03-有效的括号.py
# @Project  : AGTD


# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 1. 左括号必须用相同类型的右括号闭合。
# 2. 左括号必须以正确的顺序闭合。
# 3. 注意空字符串可被认为是有效字符串。


class Solution(object):

    # 1. 仅使用栈，更省空间
    def isValid(self, s):
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif stack and stack[-1] == item:
                stack.pop()
            else:
                return False
        return not stack

    # 2. 使用字典
    def isValidDitto(self, s):
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif stack and stack[-1] == item:
                stack.pop()
            else:
                return False

        return not stack


if __name__ == '__main__':
    str1 = "(()[]{}[])"

    s = Solution()
    res = s.isValid(str1)
    res1 = s.isValidDitto(str1)
    print(res, res1)