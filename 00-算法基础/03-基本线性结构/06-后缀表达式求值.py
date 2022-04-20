#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.16 14:57
# @File     : 06-后缀表达式求值.py
# @Project  : AGTD


def postfixEval(postfixExpr):
    stack = []
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            stack.append(int(token))
        else:
            oper2 = stack.pop()
            oper1 = stack.pop()
            result = doMath(token, oper1, oper2)
            stack.append(result)

    return int(stack.pop())


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


if __name__ == '__main__':
    print(postfixEval('7 8 + 3 2 + / 3 *'))
