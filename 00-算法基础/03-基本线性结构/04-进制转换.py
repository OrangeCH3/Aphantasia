#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.16 10:37
# @File     : 04-进制转换.py
# @Project  : AGTD

def divideBy2(decNumber):
    remStack = []

    while decNumber > 0:
        rem = decNumber % 2
        remStack.append(rem)
        decNumber //= 2

    binStr = ""
    while remStack:
        binStr += str(remStack.pop())

    return binStr


def divideByN(decNumber, baseN):
    digits = "0123456789ABCDEF"

    remStack = []

    while decNumber > 0:
        rem = decNumber % baseN
        remStack.append(rem)
        decNumber //= baseN

    newStr = ""
    while remStack:
        newStr += digits[remStack.pop()]

    return newStr


if __name__ == '__main__':
    print(divideBy2(42))

    print(divideByN(25, 16))
    print(divideByN(25, 8))
