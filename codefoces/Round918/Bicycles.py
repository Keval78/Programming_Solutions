'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import sys
# from os import path
# from math import log2, floor, ceil, sqrt, pow, gcd
# from random import random, randint, shuffle, choice
from collections import Counter, defaultdict, deque
# from itertools import permutations, combinations
# from functools import reduce
from heapq import heapify, heappop, heappush, heapreplace
# from bisect import bisect_left, bisect_right


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

def solve():
    n, m = mi()
    edge_map = defaultdict(lambda: defaultdict(lambda: INF))
    inp = []
    for i in range(m):
        u, v, c = mi()
        inp.append((u,v,c))
        edge_map[u-1][v-1] = min(edge_map[u-1][v-1], c)
        edge_map[v-1][u-1] = min(edge_map[v-1][u-1], c)
    
    bikes = li()
    # print(edge_map)
    
    mincost = [[INF]*(1001) for i in range(n)]
    def dijkstra(s):
        heap = [(0, bikes[0], s)]
        while heap:
            # print("heap", heap)
            path_cost, bike, curr = heappop(heap)
            if curr == n-1:
                mincost[curr][bike] = min(mincost[curr][bike], path_cost)

            for adj in edge_map[curr]:
                # print(curr, adj, bike, path_cost, edge_map[curr][adj])
                new_cost = path_cost + bike*edge_map[curr][adj]
                # print(new_cost)
                if new_cost < mincost[adj][bike]:
                    mincost[adj][bike] = min(mincost[adj][bike], new_cost)
                    heappush(heap, (new_cost, min(bike, bikes[adj]), adj))

    mincost[0][bikes[0]] = 0
    dijkstra(0)
    ans = min(mincost[n-1])
    print(ans)

# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
