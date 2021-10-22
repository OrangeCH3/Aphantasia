#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.19 16:58
# @File     : 15-从前序与中序遍历序列构造二叉树.py
# @Project  : AGTD


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, preorder, inorder):
        # 1. 特殊情况，树为空（递归终止条件）
        if not preorder:
            return None

        # 2. 前序遍历的第一个点就是当前的中间节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 3. 找切割点
        cut_idx = inorder.index(root_val)

        # 4. 切割inorder数组，得到左右半边
        inorder_left = inorder[:cut_idx]
        inorder_right = inorder[cut_idx+1:]

        # 5. 切割preorder数组，得到左右半边
        preorder_left = preorder[1: 1+len(inorder_left)]
        preorder_right = preorder[1+len(inorder_left):]

        # 6. 递归
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root

