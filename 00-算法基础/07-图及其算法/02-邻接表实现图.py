#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OrangeCH3
# @Time     : 2022.04.19 9:01
# @File     : 02-邻接表实现图.py
# @Project  : AGTD


class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' →connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph(object):

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nf = self.addVertex(f)
        if t not in self.vertList:
            nt = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(1, 8):
        g.addVertex(i)
    # print(g.vertList)
    for i in range(1, 8):
        print(i, ':', g.vertList[i])

    g.addEdge(1, 5, 4)
    g.addEdge(1, 7, 7)
    g.addEdge(2, 6, 2)
    g.addEdge(3, 4, 8)
    for v in g:
        for w in v.getConnections():
            print("(%s, %s)" % (v.getId(), w.getId()))

    print(g.getVertices())
    for i in range(1, 8):
        print(i, ':', g.vertList[i])
