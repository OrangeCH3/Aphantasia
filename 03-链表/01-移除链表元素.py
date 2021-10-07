#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.09.29 16:43
# @File     : 01-移除链表元素.py
# @Project  : AGTD


# 删除链表中等于给定值 val 的所有节点

# 说明: 力扣网页端与PYCharmIDE代码书写格式不同

# 1. 此种写法可在PYCharmIDE编译通过
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        cur = ListNode(0)  # 虚拟头结点
        cur.next = head
        p = cur
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return cur.next


if __name__ == '__main1__':

    l1 = ListNode(1)
    l1.next = l11 = ListNode(2)
    l11.next = l12 = ListNode(3)
    l12.next = l13 = ListNode(4)
    s = Solution()
    num = s.remove_elements(l1, 1)
    while num:
        print(num.val, end="")
        num = num.next


# -------分割线-------

# 2. 此种写法可在力扣网页端编译通过
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class SolutionDitto:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head) #添加一个虚拟节点
        cur = dummy_head
        while(cur.next!=None):
            if(cur.next.val == val):
                cur.next = cur.next.next #删除cur.next节点
            else:
                cur = cur.next
        return dummy_head.next


if __name__ == '__main2__':
    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    s1 = SolutionDitto()
    head_new = s1.removeElements(head, val)
    print(head_new)
