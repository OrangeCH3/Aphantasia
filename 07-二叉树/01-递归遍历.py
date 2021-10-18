#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.15 16:01
# @File     : 01-递归遍历.py
# @Project  : AGTD


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution(object):

    # 前序遍历
    def preorderTraversal(self, root):
        result = []

        def traversal(node):
            if node == None:
                return
            result.append(node.val)
            traversal(node.left)
            traversal(node.right)

        traversal(root)
        return result

    # 中序遍历
    def inorderTraversal(self, root):
        result = []

        def traversal(node):
            if node == None:
                return
            traversal(node.left)
            result.append(node.val)
            traversal(node.right)

        traversal(root)
        return result

    # 后序遍历
    def postorderTraversal(self, root):
        result = []

        def traversal(node):
            if node == None:
                return
            traversal(node.left)
            traversal(node.right)
            result.append(node.val)

        traversal(root)
        return result
