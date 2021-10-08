#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.07 15:06
# @File     : 05-删除链表的倒数第N个节点.py
# @Project  : AGTD


# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 进阶：你能尝试使用一趟扫描实现吗？


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        head_dummy = ListNode()
        head_dummy.next = head

        slow, fast = head_dummy, head_dummy
        # fast先往前走n步
        while (n!=0):
            fast = fast.next
            n -= 1
        while (fast.next != None):
            slow = slow.next
            fast = fast.next

        # fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next

        return head_dummy.next
