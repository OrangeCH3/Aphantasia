#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.18 10:01
# @File     : 05-对称二叉树.py
# @Project  : AGTD
import collections


class Solution(object):

    # 递归法
    def isSymmetric(self, root):
        if not root:
            return True
        return self.compare(root.left, root.right)
    def compare(self, left, right):
        # 1. 首先排除空节点的情况
        if not left and right: return False
        if left and not right: return False
        if not left and not right: return True

        # 2. 排除了空节点，再排除数值不相同的情况
        elif left.val != right.val: return False

        # 3. 最后判断左右节点都不为空，且数值相同的情况
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSame = outside and inside
        return isSame

    # 迭代法： 使用队列
    def isSymmetricDitto(self, root):
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            leftnode = queue.popleft()
            rightnode = queue.popleft()
            if not leftnode and not rightnode:
                continue  # 注意：必须为continue
            if not leftnode or not rightnode or leftnode.val != rightnode.val:
                return False
            queue.append(leftnode.left)
            queue.append(rightNode.right)
            queue.append(leftNode.right)
            queue.append(rightNode.left)
        return True

    # 迭代法：使用栈
    def isSymmetricDittoo(self, root):
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            leftnode = stack.pop()
            rightnode = stack.pop()
            if not leftNode and not rightNode:
                continue  # 注意：必须为continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            st.append(leftNode.left)
            st.append(rightNode.right)
            st.append(leftNode.right)
            st.append(rightNode.left)
        return True
