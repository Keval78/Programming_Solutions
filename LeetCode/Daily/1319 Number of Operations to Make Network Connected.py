from typing import List


class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # print(x, y)
        px, py = self.find(x), self.find(y)
        # print(px, py)
        if px == py:
            return True
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.rank[py] += 1
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        # print(self.rank, self.parent)
        return False


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        djset = DisjointSet(n)

        extracables = 0
        for u, v in connections:
            if djset.union(u, v):
                extracables += 1

        cmpnts = 0
        for i in range(n):
            if i == djset.parent[i]:
                cmpnts += 1

        # print(extracables, cmpnts)
        return cmpnts-1 if extracables >= cmpnts-1 else -1
