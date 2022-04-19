#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.20 10:34
# @File     : 17-最大二叉树.py
# @Project  : AGTD


# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
# 1. 二叉树的根是数组中的最大元素。
# 2. 左子树是通过数组中最大值左边部分构造出的最大二叉树。
# 3. 右子树是通过数组中最大值右边部分构造出的最大二叉树。
# 通过给定的数组构建最大二叉树，并且输出这个树的根节点。


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxvalue = max(nums)
        index = nums.index(maxvalue)

        root = TreeNode(maxvalue)

        left = nums[:index]
        right = nums[index + 1:]

        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root
