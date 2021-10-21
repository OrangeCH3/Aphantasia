#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.19 10:40
# @File     : 11-左叶子之和.py
# @Project  : AGTD


class Solution(object):

    # 递归法
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        leftLeft = self.sumOfLeftLeaves(root.left)  # 左
        rightLeft = self.sumOfLeftLeaves(root.right)  # 右

        leftVal = 0
        if root.left and not root.left.left and not root.left.right:
            leftVal = root.left.val  # 中

        return leftVal + leftLeft + rightLeft

    # 迭代法
    def sumOfLeftLeavesDitto(self, root):
        stack = []
        if root:
            stack.append(root)
        res = 0

        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res
