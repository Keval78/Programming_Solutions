"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def rhombuswalk(self, i, j, size, grid):
        # (i, j) is the top corner of the rhombus
        total = 0
        j1 = j2 = j
        for k in range(2*size-1):
            if j1 == j2:
                total += grid[i][j1]
            else:
                total += grid[i][j1] + grid[i][j2]
            if k < size-1:
                j1, j2 = j1-1, j2+1
            else:
                j1, j2 = j1+1, j2-1
            i += 1
        return total

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        n, m = len(grid), len(grid[0])
        heap = []
        for i in range(n):
            for j in range(m):
                # i, j = 0, 1
                # k is the size of the rhombus.
                k = min(j+1, m-j, (n-i+1)//2)
                # print(i, j, k)
                for size in range(1, k+1):
                    total = self.rhombuswalk(i, j, size, grid)
                    if total in heap:
                        continue
                    heappush(heap, total)
                    if len(heap) > 3:
                        heappop(heap)
        heap.sort(reverse=True)
        return heap
