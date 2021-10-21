#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.19 16:11
# @File     : 12-找树左下角的值.py
# @Project  : AGTD


import collections


class Solution(object):

    # 层序遍历
    def findBottomLeftValue(self, root):
        queue = collections.deque()
        if root:
            queue.append(root)
        result = 0

        while queue:
            lenth = len(queue)
            for i in range(lenth):
                if i == 0:
                    result = queue[i].val
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return result

    # 递归法(不推荐)
    def findBottomLeftValueDitto(self, root):
        max_depth = -float("INF")
        leftmost_val = 0

        def __traverse(root, cur_depth):
            nonlocal max_depth, leftmost_val
            if not root.left and not root.right:
                if cur_depth > max_depth:
                    max_depth = cur_depth
                    leftmost_val = root.val
            if root.left:
                cur_depth += 1
                __traverse(root.left, cur_depth)
                cur_depth -= 1
            if root.right:
                cur_depth += 1
                __traverse(root.right, cur_depth)
                cur_depth -= 1

        __traverse(root, 0)
        return leftmost_val