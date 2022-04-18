#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.16 10:20
# @File     : 03-简单括号匹配.py
# @Project  : AGTD

def parChecker(symbolString):
    stack = []
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            stack.append(symbol)
        else:
            if not stack:
                balanced = False
            else:
                stack.pop()

        index += 1

    if balanced and not stack:
        return True
    else:
        return False


def multiParChecker(symbolString):
    matchDict = {"(": ")", "[": "]", "{": "}", }
    stack = []
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            stack.append(symbol)
        else:
            if not stack:
                balanced = False
            else:
                top = stack.pop()
                if matchDict[top] != symbol:
                    balanced = False

        index += 1

    if balanced and not stack:
        return True
    else:
        return False


if __name__ == '__main__':
    print(parChecker("(()))"))
    print(parChecker("(())"))
    print(parChecker(""))

    print(multiParChecker("{[()}]}"))
    print(multiParChecker("{[()]}"))
