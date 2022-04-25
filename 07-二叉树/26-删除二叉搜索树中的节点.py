#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.25 21:31
# @File     : 26-删除二叉搜索树中的节点.py
# @Project  : AGTD


class Solution(object):

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                del root
                return None
            elif root.left and not root.right:
                root = root.left
                return root
            elif not root.left and root.right:
                root = root.right
                return root
            else:
                v = root.right
                while v.left:
                    v = v.left
                v.left = root.left
                root = root.right
                return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
