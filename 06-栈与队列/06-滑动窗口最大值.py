#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.15 11:20
# @File     : 06-滑动窗口最大值.py
# @Project  : AGTD


# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值。
# 要求在线性时间复杂度内解决此题。


# 单调队列（从大到小）
class MyQueue(object):

    def __init__(self):
        self.queue = []  # 使用list来实现单调队列

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        que = MyQueue()
        result = []

        for i in range(k):
            que.push(nums[i])
        result.append(que.front())

        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())

        return result


if __name__ == '__main__':

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    s = Solution()
    res = s.maxSlidingWindow(nums, k)
    print(res)








