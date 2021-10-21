#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.19 16:42
# @File     : 14-找等于目标和的路径.py
# @Project  : AGTD


# 给定一个二叉树和一个目标和
# 找到所有从根节点到叶子节点路径总和等于给定目标和的路径。


class Solution(object):

    # 递归法
    def pathsum(self, root, targetsum):

        def traversal(node, remain):
            if not node.left and not node.right and remain == 0:
                result.append(path[:])
                return
            if not node.left and not node.right:
                return
            if node.left:
                path.append(node.left.val)
                remain -= node.left.val
                traversal(node.left, remain)
                path.pop()
                remain += node.left.val
            if node.right:
                path.append(node.right.val)
                remain -= node.right.val
                traversal(node.right, remain)
                path.pop()
                remain += node.right.val

        result, path = [], []
        if not root:
            return []
        path.append(root.val)
        traversal(root, targetsum-root.val)
        return result
