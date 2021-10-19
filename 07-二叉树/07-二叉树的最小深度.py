#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.18 15:13
# @File     : 07-二叉树的最小深度.py
# @Project  : AGTD
import collections


class Solution(object):

    # 递归法
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        depth = 10**9
        if root.left:
            depth = min(self.minDepth(root.left), depth)
        if root.right:
            depth = min(self.minDepth(root.right), depth)
        return depth + 1

    # 迭代法
    def minDepthDitto(self, root):
        if not root:
            return 0
        que = collections.deque()
        que.append(root)
        res = 1
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if not node.left and not node.right:
                    return res
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res += 1
        return res

