#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.17 9:27
# @File     : 03-谢尔宾斯基Sierpinski.py
# @Project  : AGTD


import turtle
import time


# 谢尔宾斯基三角形
def drawSierpinski(degree, points):
    colorMap = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
    drawTriangle(points, colorMap[degree])
    if degree > 0:
        drawSierpinski(degree - 1,
                       {'left': points['left'],
                        'top': getMid(points['left'], points['top']),
                        'right': getMid(points['left'], points['right'])})
        drawSierpinski(degree - 1,
                       {'left': getMid(points['left'], points['top']),
                        'top': points['top'],
                        'right': getMid(points['top'], points['right'])})
        drawSierpinski(degree - 1,
                       {'left': getMid(points['left'], points['right']),
                        'top': getMid(points['top'], points['right']),
                        'right': points['right']})


def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()


def getMid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


if __name__ == '__main__':
    t = turtle.Turtle()
    points = {'left': (-200, -100),
              'top': (0, 200),
              'right': (200, -100)}
    drawSierpinski(5, points)
    t.hideturtle()
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="03-Sierpinski.eps")
    turtle.done()
