'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*n
        self.size = [1]*n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]

    def union_rank(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        djset = DisjointSet(n)

        index = {}
        for i, num in enumerate(nums):
            if num in index:
                continue
            index[num] = i
            if num-1 in index:
                djset.union(i, index[num-1])
            if num+1 in index:
                djset.union(i, index[num+1])

        return max(djset.size)
