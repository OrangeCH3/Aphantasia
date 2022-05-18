#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.18 10:47
# @File     : 04-表达式解析.py
# @Project  : AGTD


import operator


class BinaryTree(object):

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# 建立表达式解析树
def buildParseTree(fpexp):
    fplist = fpexp.split()
    # print(fplist)
    pStack = []
    eTree = BinaryTree('')
    pStack.append(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.append(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.append(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

    return eTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    # 递归调用计算表达式
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


if __name__ == '__main__':
    print("Test BinaryTree:")

    # r = BinaryTree('a')
    # r.insertLeft('b')
    # r.insertRight('c')
    # print(r.getRootVal())
    # print(r.getLeftChild().getRootVal())
    # r.getLeftChild().setRootVal('bb')
    # print(r.getLeftChild().getRootVal())
    # print(r.getRightChild().getRootVal())
    # r.getRightChild().insertRight('cc')
    # print(r.getRightChild().getRightChild().getRootVal())

    fpexps = "( 3 * ( 4 + 5 ) )"
    etree = buildParseTree(fpexps)
    ans = evaluate(etree)
    print(ans)
