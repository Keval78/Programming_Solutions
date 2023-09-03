"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import deque, defaultdict
from typing import List


class TreeAncestor:
    def __init__(self, edge_map):
        n = len(edge_map)
        k = n.bit_length()+1

        # store (parent)
        depth = [-1 for i in range(n)]
        bl_table = [[0 for i in range(n)] for j in range(k)]

        que = deque([(-1, 0)])
        while que:
            parent, node = que.popleft()
            bl_table[0][node] = parent
            depth[node] = (depth[parent]+1) if parent != -1 else 0

            for adj, w in edge_map[node]:
                if depth[adj] == -1:
                    que.append((node, adj))
        # print(depth)

        for i in range(1, k):
            for j in range(n):
                bl_table[i][j] = bl_table[i-1][bl_table[i-1][j]]

        # for bl in bl_table:
        #     print(bl)

        self.bl_table = bl_table
        self.depth = depth
        self.k = k

    def getKthAncestor(self, node, k):
        # print(node, k)
        j = 0
        while k > 0:
            if k & 1:
                node = self.bl_table[j][node]
            k = k >> 1
            j += 1
        return node

    def LCA(self, p, q):
        if self.depth[p] < self.depth[q]:
            p, q = q, p
        k = self.depth[p] - self.depth[q]
        p = self.getKthAncestor(p, k)
        if p == q:
            return p

        for i in range(self.k-1, -1, -1):
            if self.bl_table[i][p] != self.bl_table[i][q]:
                p, q = self.bl_table[i][p], self.bl_table[i][q]

        return self.bl_table[0][p]


class Solution:
    def dfs(self, node, edge_map, weights, wstack):
        weights[node] = list(wstack)
        for adj, w in edge_map[node]:
            if len(weights[adj]) == 0:
                wstack[w] += 1
                self.dfs(adj, edge_map, weights, wstack)
                wstack[w] -= 1

    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        edge_map = defaultdict(list)
        parents = [-1 for i in range(n)]
        for u, v, w in edges:
            edge_map[u].append((v, w))
            edge_map[v].append((u, w))

        weights = [[] for i in range(n)]
        wstack = [0 for i in range(26+1)]
        self.dfs(0, edge_map, weights, wstack)

        # for w in weights:
        #     print(w)

        ta = TreeAncestor(edge_map)

        ans = []
        for p, q in queries:
            lca = ta.LCA(p, q)
            # print(lca)
            val = nodes = 0
            # print([x+y-2*z for x, y, z in zip(weights[p], weights[q], weights[lca])])
            for i, v in enumerate([x+y-2*z for x, y, z in zip(weights[p], weights[q], weights[lca])]):
                val = max(val, v)
                nodes += v
            ans.append(nodes-val)

        return ans
