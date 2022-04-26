#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.26 10:58
# @File     : 03-电话号码的字母组合.py
# @Project  : AGTD


# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1/2 不对应任何字母。

# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


class Solution(object):

    def letterCombinations(self, digits):
        res = []
        s = ""
        letterMap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        if not len(digits):
            return res

        def backtrack(digits, index, s):
            if index == len(digits):
                return res.append(s)

            digit = int(digits[index])
            letters = letterMap[digit]

            for i in range(len(letters)):
                s += letters[i]
                backtrack(digits, index+1, s)
                s = s[:-1]

        backtrack(digits, 0, s)
        return res


if __name__ == '__main__':

    str1 = "36824"
    s = Solution()
    res = s.letterCombinations(str1)
    print(res)
