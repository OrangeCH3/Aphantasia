#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.18 15:55
# @File     : 08-完全二叉树的节点个数.py
# @Project  : AGTD
import collections


class Solution(object):

    # 递归法
    def countNodes(self, root):
        if not root:
            return 0
        leftnum = self.countNodes(root.left)
        rightnum = self.countNodes(root.right)
        treenum = 1 + leftnum + rightnum
        return treenum

    # 迭代法
    def countNodesDitto(self, root):
        if not root:
            return 0
        que = collections.deque()
        que.append(root)
        result = 0
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()
                result += 1  # 记录节点数量
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return result
