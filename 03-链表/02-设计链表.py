#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2021.10.06 19:02
# @File     : 02-设计链表.py
# @Project  : AGTD


# 代码在力扣网页端可编译通过


# 在链表类中实现这些功能：
# 1. get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# 2. addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# 3. addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# 4. addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。
#    如果 index 等于链表的长度，则该节点将附加到链表的末尾。
#    如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# 5. deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。


# 单链表
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self._head = Node(0)  # 虚拟头结点
        self._count = 0  # 添加的节点数

    def get(self, index):
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        elif index > self._count:
            return

        self._count += 1

        add_node = Node(val)
        pre_node, cur_node = None, self._head
        for _ in range(index + 1):
            pre_node, cur_node = cur_node, cur_node.next
        else:
            pre_node.next, add_node.next = add_node, cur_node

    def deleteAtIndex(self, index):
        if 0 <= index < self._count:
            self._count -= 1
            pre_node, cur_node = None, self._head
            for _ in range(index + 1):
                pre_node, cur_node = cur_node, cur_node.next
            else:
                pre_node.next, cur_node.next = cur_node.next, None


# 双链表
# 相对于单链表，Node新增了prev属性
class Node2:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList2:

    def __init__(self):
        self._head, self._tail = Node2(0), Node2(0)  # 虚拟节点
        self._head.next, self._tail.next = self._tail, self._head
        self._count = 0

    def _get_node(self, index):
        # 当index小于_count//2时, 使用_head查找更快, 反之_tail更快
        if index >= self._count // 2:
            # 使用prev往前找
            node = self._tail
            for _ in range(self._count - index):
                node = node.prev

        else:
            node = self._head
            for _ in range(index + 1):
                node = node.next

        return node

    def _update(self, left, right, val):
        self._count += 1
        node = Node2(val)
        left.next, right.prev = node, node
        node.prev, node.next = left, right

    def get(self, index):
        if 0 <= index < self._count:
            node = self._get_node(index)
            return node.val
        else:
            return -1

    def addAtHead(self, val):
        self._update(self._head, self._head.next, val)

    def addAtTail(self, val):
        self._update(self._tail.prev, self._tail, val)

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        elif index > self._count:
            return
        node = self._get_node(index)
        self._update(node.prev, node, val)

    def deleteAtIndex(self, index):
        if 0 <= index < self._count:
            node = self._get_node(index)

            self._count -= 1
            node.prev.next, node.next.prev = node.next, node.prev
