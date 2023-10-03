'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import math
from typing import List
from collections import defaultdict, deque

MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)

        indegrees = [0]*n
        for i in range(n):
            indegrees[edges[i]] += 1

        leafs = [i for i in range(n) if indegrees[i] == 0]
        # print(indegrees)
        # print(leafs)

        cycles = [1] * n
        for node in leafs:
            while True:
                cycles[node] = 0
                node = edges[node]
                indegrees[node] -= 1
                if indegrees[node] != 0:
                    break
        # print(cycles)

        def dfs(i, distance, edges):
            node, cnt = i, 1
            while edges[node] != i:  # Count loop size
                node = edges[node]
                cnt += 1

            node = i
            while edges[node] != i:  # add loop size into every loop node.
                distance[node] = cnt
                node = edges[node]

        def dfs2(i, distance, edges):
            node, cnt = i, 0
            while distance[node] == 0:  # Count until non zero nodes.
                distance[node] = -cnt
                cnt += 1
                node = edges[node]
            cnt += distance[node]

            node = i
            while distance[node] <= 0:  # add count to every node.
                distance[node] += cnt
                node = edges[node]

        distance = [0]*n
        for i in range(n):
            if cycles[i] == 1 and distance[i] == 0:
                dfs(i, distance, edges)

        for i in leafs:
            dfs2(i, distance, edges)

        return distance
