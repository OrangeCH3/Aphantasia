#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.09.29 16:18
# @File     : 05-螺旋矩阵.py
# @Project  : AGTD


# 给定一个正整数 n
# 生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵

def spiral_matrix(n):

    # 初始化要填充的正方形
    matrix = [[0] * n for _ in range(n)]

    left, right, up, down = 0, n-1, 0, n-1

    number = 1  # 初始要填充的数字

    while left < right and up < down:

        # 填充原则: 左闭右开[)
        # 从左到右填充上边
        for x in range(left, right):
            matrix[up][x] = number
            number += 1

        # 从上到下填充右边
        for y in range(up, down):
            matrix[y][right] = number
            number += 1

        # 从右到左填充下边
        for z in range(right, left, -1):
            matrix[down][x] = number
            number += 1

        # 从下到上填充左边
        for w in range(down, up, -1):
            matrix[w][left] = number
            number += 1

        # 缩小一圈范围
        left += 1
        right -= 1
        up += 1
        down -= 1

    # 如果阶数为奇数，需要填充一次中心
    if n % 2:
        matrix[n // 2][n // 2] = number

    return matrix


if __name__ == '__main__':

    res = spiral_matrix(5)
    print(res)
