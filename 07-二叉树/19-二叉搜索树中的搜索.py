#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.21 9:53
# @File     : 19-二叉搜索树中的搜索.py
# @Project  : AGTD


class Solution(object):

    # 递归法
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)

        if root.val < val:
            return self.searchBST(root.right, val)

    # 迭代法
    def searchBSTDitto(self, root, val):
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return root



