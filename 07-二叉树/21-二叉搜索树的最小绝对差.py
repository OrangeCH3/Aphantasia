#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.21 15:47
# @File     : 21-二叉搜索树的最小绝对差.py
# @Project  : AGTD


class Solution(object):

    # 递归法
    def getMinimumDifference(self, root):
        res = []
        r = float("inf")

        # 把二叉搜索树转换成有序数组
        def buildList(root):
            if not root:
                return None
            # 中序遍历
            if root.left:
                buildList(root.left)
            res.append(root.val)
            if root.right:
                buildList(root.right)
            return res

        buildList(root)
        for i in range(len(res)-1):
            r = min(abs(res[i]-res[i+1]), r)

        return r

    # 迭代法
    def getMinimumDifferenceDitto(self, root):
        stack = []
        cur = root
        pre = None
        result = float("inf")

        while cur or stack:
            if cur:  # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else:  # 逐一处理节点
                cur = stack.pop()
                if pre:  # 当前节点和前节点的值的差值
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right
            return result
