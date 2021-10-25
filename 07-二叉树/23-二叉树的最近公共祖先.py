#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.25 10:54
# @File     : 23-二叉树的最近公共祖先.py
# @Project  : AGTD


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)  # 左
        right = self.lowestCommonAncestor(root.right, p, q)  # 右

        if left and right:  # 中: left和right不为空，root就是最近公共节点
            return root
        elif left and not right:  # 目标节点通过left返回
            return left
        elif not left and right:  # 目标节点通过right返回
            return right
        else:
            return None

