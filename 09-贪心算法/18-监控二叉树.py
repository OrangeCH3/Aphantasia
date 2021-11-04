#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.11.01 17:23
# @File     : 18-监控二叉树.py
# @Project  : AGTD


class Solution(object):

    def minCameraCover(self, root):

        result = 0

        def traversal(cur):
            nonlocal result  # nonlocal声明的变量不是局部变量, 也不是全局变量, 而是外部嵌套函数内的变量。

            # 0：该节点无覆盖
            # 1：本节点有摄像头
            # 2：本节点有覆盖

            if not cur:
                return 2  # 空节点则为有覆盖状态

            left = traversal(cur.left)
            right = traversal(cur.right)

            if left == 2 and right == 2:  # 情况1：左右节点都有覆盖
                return 0
            elif left == 0 or right == 0:  # 情况2：左右节点至少有一个无覆盖的情况
                result += 1
                return 1
            elif left == 1 or right == 1:  # 情况3：左右节点至少有一个有摄像头
                return 2
            else:
                return -1

        # 情况4：处理头结点未覆盖的情况
        if traversal(root) == 0:
            result += 1

        return result

