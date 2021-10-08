#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.07 15:37
# @File     : 06-链表相交.py
# @Project  : AGTD


# 给定两个（单向）链表，判定它们是否相交并返回交点。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        根据快慢法则，走的快的一定会追上走得慢的。
        在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

        那么，只要其中一个链表走完了，就去走另一条链表的路。
        如果有交点，他们最终一定会在同一个位置相遇
        :param headA: ListNode
        :param headB: ListNode
        :return: ListNode
        """
        cur_a, cur_b = headA, headB

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB  # 如果a走完了，那么就切换到b
            cur_b = cur_b.next if cur_b else headA  # 同理，b走完了就切换到a

        return cur_a
