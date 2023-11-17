'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
from collections import defaultdict


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        djset = DisjointSet(n)

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    djset.parent[j] = i
        
        for i in range(n):
            djset.find(i)

        return djset.parent[0]


grid = [[0,1],[0,0]]
ans = Solution().findChampion(grid)
print(ans)


grid = [[0,0,1],[1,0,1],[0,0,0]]
ans = Solution().findChampion(grid)
print(ans)
