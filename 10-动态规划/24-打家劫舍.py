#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.06 12:28
# @File     : 24-打家劫舍.py
# @Project  : AGTD


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def rob(self, root):
        result = self.rob_tree(root)
        return max(result[0], result[1])

    def rob_tree(self, node):
        if not node:
            return [0, 0]  # [偷当前节点金额，不偷当前节点金额]
        # 后序遍历
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        val1 = node.val + left[1] + right[1]  # 偷当前节点，不能偷子节点
        val2 = max(left[0], left[1]) + max(right[0], right[1])  # 不偷当前节点，可偷可不偷子节点
        return [val1, val2]
