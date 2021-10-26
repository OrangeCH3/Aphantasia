#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.25 11:06
# @File     : 25-二叉搜索树中的插入操作.py
# @Project  : AGTD


class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Solution(object):

    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root
