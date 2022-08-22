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
        res = []
        pre = None
        cur = root
        count = 1
        maxcnt = 0

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and pre.val == cur.val:
                    count += 1
                else:
                    count = 1

                if count == maxcnt:
                    res.append(cur.val)
                if count > maxcnt:
                    maxcnt = count
                    res.clear()
                    res.append(cur.val)

                pre = cur
                cur = cur.right

        return res

    def findModeDittoo(self, root: Optional[TreeNode]) -> List[int]:

        tmp = []

        def trv(node):
            if not node:
                return None
            trv(node.left)
            tmp.append(node.val)
            trv(node.right)

        trv(root)
        from collections import Counter
        valCnt = Counter(tmp)
        valCntSort = sorted(valCnt.items(), key=lambda x: -x[1])
        return [val for val, cnt in valCntSort if cnt == valCntSort[0][1]]
