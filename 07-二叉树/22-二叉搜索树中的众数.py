#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.21 16:37
# @File     : 22-二叉搜索树中的众数.py
# @Project  : AGTD


class Solution(object):

    # 递归法
    def __init__(self):
        self.pre = root
        self.count = 0  # 统计频率
        self.countMax = 0  # 最大频率
        self.res = []
    def findMode(self, root):

        if not root:
            return

        def findNumber(root):
            if not root:
                return None
            findNumber(root.left)  # 左
            if self.pre.val == root.val:  # 中
                self.count += 1
            else:
                self.pre = root
                self.count = 1

            if self.count > self.countMax:
                self.countMax = self.count
                self.res = [root.val]
            elif self.count == self.countMax:
                self.res.append(root.val)

            findNumber(root.right)  # 右
            return

        findNumber(root)
        return self.res

    # 迭代法-中序遍历(不使用额外空间，利用二叉搜索树特性)
    def findModeDitto(self, root):
        stack = []
        cur = root
        pre = None

        maxCount, count = 0, 0
        res = []

        while stack or cur:
            if cur:  # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left

            else:
                cur = stack.pop()

                if pre == None:
                    count = 1
                elif pre.val == cur.val:
                    count += 1
                else:
                    count = 1

                if count == maxCount:
                    res.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    res.clear()
                    res.append(cur.val)

                pre = cur
                cur = cur.right

        return res
