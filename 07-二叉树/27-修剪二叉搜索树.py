#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.25 21:44
# @File     : 27-修剪二叉搜索树.py
# @Project  : AGTD


class Solution(object):

    def trimBST(self, root, low, high):
        if not root:
            return root

        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root

