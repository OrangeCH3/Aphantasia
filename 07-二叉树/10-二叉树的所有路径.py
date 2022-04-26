#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.19 9:28
# @File     : 10-二叉树的所有路径.py
# @Project  : AGTD


class Solution(object):

    def binaryTreePaths(self, root):
        res = []
        path = []

        def backtrace(node):

            path.append(str(node.val))

            if not node.left and not node.right:
                res.append(path[:])
                return

            ways = []

            if node.left: ways.append(node.left)
            if node.right: ways.append(node.right)

            for way in ways:
                backtrace(way)
                path.pop()

        backtrace(root)

        return ['->'.join(val) for val in res]