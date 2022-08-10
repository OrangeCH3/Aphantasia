#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.19 9:18
# @File     : 04-DFS求解骑士周游KnightTour.py
# @Project  : AGTD


import sys
import os
import time


class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(
            self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

    def getId(self):
        return self.id


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, 2), (-1, -2), (1, -2), (1, 2),
                   (2, 1), (-2, 1), (2, -1), (-2, -1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if 0 <= x < bdSize:
        return True
    else:
        return False


def knightGraph(bdSize):
    ktg = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositons = genLegalMoves(row, col, bdSize)
            for e in newPositons:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktg.addEdge(nodeId, nid)
    return ktg


def posToNodeId(row, col, bdSize):
    return row * bdSize + col


def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


def knightTourBetter(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


if __name__ == '__main__':
    ktg = knightGraph(8)
    edgeCount = 0
    for v in ktg:
        for w in v.getConnections():
            edgeCount += 1
    print(edgeCount)  # 共有336条边，相比与全连接邻接矩阵4096条边，仅占其8.2%，是稀疏图
    print()

    ktg = knightGraph(5)
    path = []
    start = ktg.getVertex(4)
    t0 = time.time()
    knightTour(0, path, start, 24)
    for i, v in enumerate(path):
        if i == 24:
            print(v.getId())
        else:
            print(v.getId(), end='→')
    print("(5 × 5) knightTour use: ", time.time() - t0)
    print()

    ktg = knightGraph(5)
    path = []
    start = ktg.getVertex(4)
    t1 = time.time()
    knightTourBetter(0, path, start, 24)
    for i, v in enumerate(path):
        if i == 24:
            print(v.getId())
        else:
            print(v.getId(), end='→')
    print("(5 × 5) knightTourBetter use: ", time.time() - t1)
    print()

    ktg = knightGraph(6)
    path = []
    start = ktg.getVertex(4)
    t2 = time.time()
    knightTour(0, path, start, 35)
    for i, v in enumerate(path):
        if i == 35:
            print(v.getId())
        else:
            print(v.getId(), end='→')
    print("(6 × 6) knightTour use: ", time.time() - t2)
    print()

    ktg = knightGraph(6)
    path = []
    start = ktg.getVertex(4)
    t3 = time.time()
    knightTourBetter(0, path, start, 35)
    for i, v in enumerate(path):
        if i == 35:
            print(v.getId())
        else:
            print(v.getId(), end='→')
    print("(6 × 6) knightTourBetter use: ", time.time() - t3)
