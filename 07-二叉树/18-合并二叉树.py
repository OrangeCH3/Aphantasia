#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.21 9:34
# @File     : 18-合并二叉树.py
# @Project  : AGTD
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # 递归法
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1

        # 重复使用了题目给出的节点而不是创建新节点。节省时间和空间
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

    # 迭代法
    def mergeTreesDitto(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1

        queue = collections.deque()
        queue.append(root1)
        queue.append(root2)

        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()

            # 更新queue
            # 只有两个节点都有左节点时, 再往queue里面放.
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            # 只有两个节点都有右节点时, 再往queue里面放.
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)

            # 更新当前节点. 同时改变当前节点的左右孩子.
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right

        return root1
