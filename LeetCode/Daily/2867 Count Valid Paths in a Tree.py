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


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]):
        # A path (a, b) is valid if there exists exactly one prime number among the node labels in the path from a to b.
        primes = [i for i in range(n+1)]
        primes[1] = 0

        def sieve(n):
            p = 2
            while p*p <= n:
                if primes[p]:
                    for i in range(p*p, n+1, p):
                        primes[i] = 0
                p += 1
        sieve(n)

        def isprime(x):
            return primes[x] != 0

        dsu = DisjointSet(n+1)
        edge_map = defaultdict(list)

        for u, v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)

            if isprime(u) or isprime(v):
                continue
            dsu.union(u, v)

        res = 0
        for i in range(n+1):
            if not isprime(i):
                continue
            # If number is prime.
            # Ans = SUM(subtree_nodes) + SUM(child * (SUM(subtree_nodes) - child)) // 2

            subtree_count = 0
            subtree_nodes = []
            for adj in edge_map[i]:
                if isprime(adj):
                    continue
                nodes = dsu.size[dsu.find(adj)]
                subtree_nodes.append(nodes)
                subtree_count += nodes

            ans = 0
            for nodes in subtree_nodes:
                ans += nodes * (subtree_count - nodes)

            res += subtree_count + ans//2

        print(res)


n = 2
edges = [[2, 1]]
Solution().countPaths(n, edges)

# n = 6
# edges = [[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]]
# Solution().countPaths(n, edges)
# Proeblem Link: https://leetcode.com/problems/count-valid-paths-in-a-tree/description/
