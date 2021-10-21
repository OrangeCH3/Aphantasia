#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.19 16:18
# @File     : 13-路径总和.py
# @Project  : AGTD


# 给定一个二叉树和一个目标和
# 判断该树中是否存在根节点到叶子节点的路径
# 这条路径上所有节点值相加等于目标和。


class Solution(object):

    # 递归法
    def haspathsum(self, root, targetsum):
        def isornot(root, targetsum):
            if not root.left and not root.right and targetsum == 0:
                return True
            if not root.left and not root.right:
                return False
            if root.left:
                targetsum -= root.left.val
                if isornot(root.left, targetsum): return True
                targetsum += root.left.val  # 回溯
            if root.right:
                targetsum -= root.right.val
                if isornot(root.right, targetsum): return True
                targetsum += root.right.val  # 回溯
            return False

        if not root:
            return False
        else:
            return isornot(root, targetsum-root.val)

    # 迭代-层序遍历(不推荐)
    def haspathsumDitto(self, root, targetsum):
        if not root:
            return False
        stack = [(root, root.val)]  # [(当前节点，路径数值), ...]

        while stack:
            node, pathsum = stack.pop()

            if not node.left and not node.right and pathsum == targetsum:
                return True

            if node.right:
                stack.append((node.right, pathsum+node.right.val))

            if node.left:
                stack.append((node.left, pathsum+node.left.val))

        return False