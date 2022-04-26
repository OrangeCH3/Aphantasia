#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.30 12:37
# @File     : 15-解数独.py
# @Project  : AGTD


class Solution(object):

    def solveSudoku(self, board):

        def siValid(row, col, val, board):
            for i in range(9):  # 判断行里是否重复
                if board[row][i] == str(val):
                    return False
            for j in range(9):  # 判断列里是否重复
                if board[j][col] == str(val):
                    return False
            startRow = (row // 3) * 3
            startCol = (col // 3) * 3
            for i in range(startRow, startRow + 3):  # 判断9方格里是否重复
                for j in range(startCol, startCol + 3):
                    if board[i][j] == str(val):
                        return False
            return True

        def backtarck(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != ".":
                        continue
                    for k in range(1, 10):
                        if siValid(i, j, k, board):
                            board[i][j] = str(k)
                            if backtarck(board):
                                return True
                            board[i][j] = "."
                    return False  # 9个数都试完了，都不行，那么就返回false
            return True  # 遍历完没有返回false，说明找到了合适棋盘位置了

        backtarck(board)


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s = Solution()
    s.solveSudoku(board)
    print(board)
