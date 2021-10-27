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


class Solution(object):

    def BST2AccumuTree(self, root):

        def buildalist(root):
            if not root:
                return None

            buildalist(root.right)
            root.val += self.pre
            self.pre = root.val
            buildalist(root.left)

        self.pre = 0
        buildalist(root)
        return root

