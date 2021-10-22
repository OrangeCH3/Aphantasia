#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.20 10:09
# @File     : 16-从中序与后序遍历序列构造二叉树.py
# @Project  : AGTD


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, inorder, postorder):
        # 1. 特殊情况，树为空（递归终止条件）
        if not postorder:
            return None

        # 2. 后序遍历的最后一个点就是当前的中间节点
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 3. 找切割点
        cut_idx = inorder.index(root_val)

        # 4. 切割inorder数组，得到左右半边
        inorder_left = inorder[:cut_idx]
        inorder_right = inorder[cut_idx+1:]

        # 5. 切割postorder数组，得到左右半边
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_right):-1]

        # 6. 递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

