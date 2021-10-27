#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.25 21:55
# @File     : 28-将有序数组转换为二叉搜索树.py
# @Project  : AGTD


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def sortedArrayToBST(self, nums):

        def buildTree(left, right):
            if left > right:   # 左闭右闭的区间，当区间 left > right的时候，就是空节点,当left = right的时候，不为空
                return None

            mid = left + (right - left) // 2  # 保证数据不会越界
            val = nums[mid]

            root = TreeNode(val)
            root.left = buildTree(left, mid-1)
            root.right = buildTree(mid+1, right)

            return root

        root = buildTree(0, len(nums)-1)  # 左闭右闭区间
        return root
