#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.25 22:07
# @File     : 29-把二叉搜索树转换为累加树.py
# @Project  : AGTD


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = TreeNode(0)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bulidGST(node):
            if not node:
                return node
            bulidGST(node.right)
            node.val += self.pre.val
            self.pre = node
            bulidGST(node.left)

        bulidGST(root)
        return root
