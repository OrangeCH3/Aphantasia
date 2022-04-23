#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.14 16:57
# @File     : 05-逆波兰表达式求值.py
# @Project  : AGTD


# 逆波兰表达式：是一种后缀表达式，所谓后缀就是指算符写在后面。
# 逆波兰表达式主要有以下两个优点：
# 1. 去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
# 2. 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。


class Solution(object):

    def evalRPN(self, tokens):
        stack = []
        for item in tokens:
            if item not in {'+', '-', '*', '/'}:  # in 操作符用于判断键是否存在于字典中
                stack.append(item)
            else:
                right, left = stack.pop(), stack.pop()
                tmp = int(eval(f'{left} {item} {right}'))  # 必须用int来接 题目要求除法只保留整数部分
                stack.append(tmp)

        return int(stack.pop())


if __name__ == '__main__':
    list1 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

    s = Solution()
    res = s.evalRPN(list1)
    print(res)
