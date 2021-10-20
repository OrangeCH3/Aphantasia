#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.19 9:28
# @File     : 10-二叉树的所有路径.py
# @Project  : AGTD


class Solution(object):

    def binaryTreePaths(self, root):
        initpath = []
        result = []

        def backtrace(node, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                res.append(path[:])
            ways = []
            if node.left: ways.append(node.left)
            if node.right: ways.append(node.right)
            for way in ways:
                backtrace(way, path)
                path.pop()  # 回溯

        backtrace(root, initpath)
        return ['->'.join(list(map(str, i))) for i in res]
