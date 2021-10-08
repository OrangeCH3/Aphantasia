#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.07 15:56
# @File     : 07-环形链表.py
# @Project  : AGTD


# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next

                return p
        return None

