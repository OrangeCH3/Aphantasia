#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.14 16:46
# @File     : 04-删除字符串中的所有相邻重复项.py
# @Project  : AGTD


# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。


class Solution(object):

    # 方法一，使用栈，推荐！
    def removeDuplicates(self, s):
        res = list()
        for item in s:
            if res and res[-1] == item:
                res.pop()
            else:
                res.append(item)
        return ''.join(res)

    # 方法二，使用双指针模拟栈，如果不让用栈可以作为备选方法。
    def removeDuplicatesDitto(self, s):
        res = list(s)
        slow = fast = 0
        lenth = len(res)

        while fast < lenth:
            res[slow] = res[fast]

            if slow > 0 and res[slow] == res[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[0:slow])


if __name__ == '__main__':
    str1 = "abbascaacl"

    s = Solution()
    res = s.removeDuplicates(str1)
    res1 = s.removeDuplicatesDitto(str1)

    print(res, res1)
