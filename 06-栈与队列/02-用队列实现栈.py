#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.14 14:30
# @File     : 02-用队列实现栈.py
# @Project  : AGTD


# 使用队列实现栈的下列操作：
# 1. push(x) -- 元素 x 入栈
# 2. pop() -- 移除栈顶元素
# 3. top() -- 获取栈顶元素
# 4. empty() -- 返回栈是否为空


from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Python普通的Queue或SimpleQueue没有类似于peek的功能
        也无法用索引访问，在实现top的时候较为困难。

        用list可以，但是在使用pop(0)的时候时间复杂度为O(n)
        因此这里使用双向队列，我们保证只执行popleft()和append()，因为deque可以用索引访问，可以实现和peek相似的功能

        in - 存所有数据
        out - 仅在pop的时候会用到
        """
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x):
        """

        :param x: int
        :return: None
        """
        self.queue_in.append(x)

    def pop(self):
        """
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个

        tip：这不能像栈实现队列一样，因为另一个queue也是FIFO，如果执行pop()它不能像
        stack一样从另一个pop()，所以干脆in只用来存数据，pop()的时候两个进行交换
        :return: int
        """
        if self.empty():
            return True

        for i in range(len(self.queue_in)-1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()

    def top(self):
        """
        1. 首先确认不空
        2. 我们仅有in会存放数据，所以返回第一个即可
        :return: int
        """
        if self.empty():
            return None
        return self.queue_in[-1]

    def empty(self):
        """
        因为只有in存了数据，只要判断in是不是有数即可
        :return: bool
        """
        return not self.queue_in

