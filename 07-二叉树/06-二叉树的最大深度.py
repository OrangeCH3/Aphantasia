#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.18 11:25
# @File     : 06-二叉树的最大深度.py
# @Project  : AGTD
import collections


class Solution(object):

    # 二叉树-递归法
    def maxBinaryDepth(self, root):
        if not root:
            return 0
        leftdepth = self.maxBinaryDepth(root.left)  # 左
        rightdepth = self.maxBinaryDepth(root.right)  # 右
        depth = max(leftdepth, rightdepth)  # 中
        return depth + 1

    # 二叉树-迭代法
    def maxBinaryDepthDitto(self):
        if not root:
            return 0
        depth = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            depth += 1
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

    # N叉树-递归法
    def maxNDepth(self, root):
        if not root:
            return 0
        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxNDepth(root.children[i]))
        return depth + 1

    # N叉树-迭代法
    def maxNDepthDitto(self, root):
        if not root:
            return 0
        depth = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.popleft()
                for j in range(len(node.children)):
                    if node.children[j]:
                        queue.append(node.children[j])

        return depth

