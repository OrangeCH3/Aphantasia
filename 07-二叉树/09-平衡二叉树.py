#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.18 17:12
# @File     : 09-平衡二叉树.py
# @Project  : AGTD


class Solution(object):

    # 递归法
    def isBalanced(self, root):
        return True if self.getDepth(root) != -1 else False
    def getDepth(self, node):
        if not node:
            return 0
        leftdepth = self.getDepth(node.left)
        if leftdepth == -1: return -1
        rightdepth = self.getDepth(node.right)
        if rightdepth == -1: return -1
        return -1 if abs(leftdepth - rightdepth) > 1 else 1 + max(leftdepth, rightdepth)

    # 迭代法(不推荐)
    def isBalancedDitto(self, root: TreeNode) -> bool:
        st = []
        if not root:
            return True
        st.append(root)
        while st:
            node = st.pop()  # 中
            if abs(self.getDepthDitto(node.left) - self.getDepthDitto(node.right)) > 1:
                return False
            if node.right:
                st.append(node.right)  # 右（空节点不入栈）
            if node.left:
                st.append(node.left)  # 左（空节点不入栈）
        return True
    def getDepthDitto(self, cur):
        st = []
        if cur:
            st.append(cur)
        depth = 0
        result = 0
        while st:
            node = st.pop()
            if node:
                st.append(node)  # 中
                st.append(None)
                depth += 1
                if node.right: st.append(node.right)  # 右
                if node.left: st.append(node.left)  # 左
            else:
                node = st.pop()
                depth -= 1
            result = max(result, depth)
        return result

