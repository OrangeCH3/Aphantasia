#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.30 12:18
# @File     : 14-N皇后.py
# @Project  : AGTD


class Solution(object):

    def solveNQueens(self, n):
        if not n:
            return []
        board = [["."] * n for _ in range(n)]
        res = []

        def isVaild(board, row, col):
            # 判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            # 判断左上角是否冲突
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否冲突
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(board, row, n):
            # 如果走到最后一行，说明已经找到一个解：
            if row == n:
                tmp_res = []
                for item in board:
                    tmp_str = "".join(item)
                    tmp_res.append(tmp_str)
                res.append(tmp_res)
            for col in range(n):
                if not isVaild(board, row, col):
                    continue
                board[row][col] = "Q"
                backtrack(board, row+1, n)
                board[row][col] = "."

        backtrack(board, 0, n)
        return res


if __name__ == '__main__':
    n = 4
    s = Solution()
    res = s.solveNQueens(n)
    print(res)

