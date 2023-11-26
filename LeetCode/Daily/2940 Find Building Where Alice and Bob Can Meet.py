'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import defaultdict
from heapq import heapify, heappop, heappush, heapreplace

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = [-1] * n
        nqueries = defaultdict(list)
        for idx in range(n):
            i, j = min(queries[idx]), max(queries[idx])
            if i==j or (j > i and heights[j] > heights[i]):
                ans[idx] = j
            else:
                nqueries[max(i, j)].append((max(heights[i], heights[j]), idx))
        
        j = 0
        heap = []
        for idx, height in enumerate(heights):
            for v in nqueries[idx]:
                heappush(heap, v)

            while heap and height > heap[0][0]:
                val, query = heappop(heap)
                ans[query] = idx

        return ans


heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
ans = Solution().leftmostBuildingQueries(heights, queries)
print(ans)

heights = [5,3,8,2,6,1,4,6]
queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
ans = Solution().leftmostBuildingQueries(heights, queries)
print(ans)
