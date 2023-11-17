'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
from collections import defaultdict, deque


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Use Topological sorting to find loop in the graph.
        indegrees = [0 for i in range(n)]
        edge_map = defaultdict(list)
        for u, v in edges:
            indegrees[v] += 1
            edge_map[u].append(v)
        
        que = deque()
        for i in range(n):
            if indegrees[i] == 0:
                que.append(i)
        
        tp_sorting = []
        while len(que):
            node = que.popleft()
            tp_sorting.append(node)
            for adj in edge_map[node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    que.append(adj)
        
        if len(tp_sorting) != n: return -1
        
        # Use Disjoint set to find end parent of each node.
        djset = DisjointSet(n)
        for u, v in edges:
            djset.parent[v] = u
        for i in range(n):
            djset.find(i)

        if len(set(djset.parent)) == 1:
            return djset.parent[0]
        else:
            return -1


n = 3
edges = [[0,1],[1,2]]
ans = Solution().findChampion(n, edges)
print(ans)


n = 4
edges = [[0,2],[1,3],[1,2]]
ans = Solution().findChampion(n, edges)
print(ans)

n = 3
edges = [[0,1],[1,2],[2,0]]
ans = Solution().findChampion(n, edges)
print(ans)
