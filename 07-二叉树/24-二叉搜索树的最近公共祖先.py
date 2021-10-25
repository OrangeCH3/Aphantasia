#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.25 11:00
# @File     : 24-二叉搜索树的最近公共祖先.py
# @Project  : AGTD


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):

        if not root:  # 中
            return root

        if root.val > p.val and root.val > q.val:  # 左
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:  # 右
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

