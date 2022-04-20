#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.16 14:40
# @File     : 05-中缀转后缀.py
# @Project  : AGTD


def infixToPostfix(infixexpr):

    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    opStack, postList = [], []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postList.append(token)
        elif token == "(":
            opStack.append(token)
        elif token == ")":
            top = opStack.pop()
            while top != "(":
                postList.append(top)
                top = opStack.pop()
        else:
            while opStack and prec[opStack[-1]] >= prec[token]:
                postList.append(opStack.pop())
            opStack.append(token)

    while opStack:
        postList.append(opStack.pop())

    return " ".join(postList)


if __name__ == '__main__':
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
