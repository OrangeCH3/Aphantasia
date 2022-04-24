#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 9:24
# @File     : 02-分形树FractalTree.py
# @Project  : AGTD


import turtle
import time


# 递归可视化
def drawSpiral(t, linLen):
    if linLen > 0:
        t.forward(linLen)
        t.right(90)
        drawSpiral(t, linLen - 5)


# 画分形树
def drawTree(branchLen):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        drawTree(branchLen - 15)
        t.left(40)
        drawTree(branchLen - 15)
        t.right(20)
        t.backward(branchLen)


if __name__ == '__main__':
    # t = turtle.Turtle()
    # t.hideturtle()
    # drawSpiral(t, 100)
    # turtle.done()

    t = turtle.Turtle()
    # t.hideturtle()
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    t.pencolor('green')
    t.pensize(2)
    drawTree(75)
    turtle.done()
