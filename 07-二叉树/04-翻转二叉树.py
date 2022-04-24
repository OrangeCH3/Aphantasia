#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.17 17:05
# @File     : 04-翻转二叉树.py
# @Project  : AGTD


# 翻转一棵二叉树。


from collections import deque

class Solution(object):

    # 递归法，前序遍历
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left  # 中
        self.invertTree(root.left)  # 左
        self.invertTree(root.right)  # 右
        return root

    # 迭代法，前序遍历
    def invertTreeDitto(self, root):
        if not root:
            return None
        st = [root]
        while st:
            node = st.pop()
            node.left, node.right = node.right, node.left  # 中
            if node.right:
                st.append(node.right)  # 右先入栈
            if node.left:
                st.append(node.left)  # 左后入栈
        return root

    # 迭代法，层序遍历
    def invertTreeDittoo(self, root):
        if not root:
            return
        que = deque([root])
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                node.left, node.right = node.right, node.left  # 节点处理
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
