#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.14 14:20
# @File     : 01-用栈实现队列.py
# @Project  : AGTD


# 使用栈实现队列的下列操作：
# 1. push(x) -- 将一个元素放入队列的尾部。
# 2. pop() -- 从队列首部移除元素。
# 3. peek() -- 返回队列首部的元素。
# 4. empty() -- 返回队列是否为空。


class Solution(object):

    def __init__(self):
        """
        in主要负责push，out主要负责pop
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        有新元素进来，就往in里面push
        :param x: int
        :return: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :return: int
        """
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        Get the front element.
        :return: int
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):
        """
        只要in或者out有元素，说明队列不为空
        :return: bool
        """
        return not (self.stack_in or self.stack_out)


