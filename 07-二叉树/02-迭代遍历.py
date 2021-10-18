#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.17 13:08
# @File     : 02-迭代遍历.py
# @Project  : AGTD


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution(object):

    # 前序遍历
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # 后序遍历
    def postorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]

    # 中序遍历
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = []
        result = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result

