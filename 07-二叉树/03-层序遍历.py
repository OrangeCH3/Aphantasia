#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.17 16:38
# @File     : 03-层序遍历.py
# @Project  : AGTD

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution(object):

    # 迭代法
    def levelOrder(self, root):
        results = []
        if not root:
            return results

        que = deque([root])

        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results

    # 递归法
    def levelOrderDitto(self, root):
        res = []

        def helper(root, depth):
            if not root:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)

        helper(root, 0)
        return res
