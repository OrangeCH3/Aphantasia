#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.21 15:06
# @File     : 20-验证二叉搜索树.py
# @Project  : AGTD


class Solution(object):

    # 递归法-中序遍历
    def isValidBST(self, root):

        tmp_list = []

        def __traverse(root):
            nonlocal tmp_list
            if not root:
                return
            __traverse(root.left)
            tmp_list.append(root.val)
            __traverse(root.right)

        def __is_sorted(nums):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    return False
            return True

        __traverse(root)
        res = __is_sorted(tmp_list)

        return res

    # 迭代法-中序遍历
    def isValidBSTDitto(self, root):
        stack = []
        cur = root
        pre = None

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and cur.val <= pre.val:
                    return False
                pre = cur
                cur = cur.right
        return True

