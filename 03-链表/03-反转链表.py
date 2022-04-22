#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.07 14:39
# @File     : 03-反转链表.py
# @Project  : AGTD


# 代码在力扣网页端可编译通过


# 反转一个单链表。


# 1. 双指针
def reverseLinkedList(head):

    cur = head
    pre = None  # 必须是 None 值

    while cur != None:
        tmp = cur.next

        cur.next = pre

        # 更新pre、cur指针
        pre = cur
        cur = tmp

    return pre


# 2. 递归法
def reverseLinkedList2(head):

    def reverse(pre, cur):
        if not cur:
            return pre

        tmp = cur.next
        cur.next = pre

        return reverse(cur, tmp)

    return reverse(None, head)
