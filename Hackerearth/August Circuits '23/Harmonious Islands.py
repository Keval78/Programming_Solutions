'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import math
import sys
# from os import path
# from math import log2, floor, ceil, sqrt, pow, gcd
# from random import random, randint, shuffle, choice
# from collections import Counter, defaultdict, deque
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


def dijkstra(edge_map, src, n):
    heap = [(0, src)]
    dist = [INF for _ in range(n+1)]
    dist[src % (n+1)] = 0
    while heap:
        cost, node = heappop(heap)
        if dist[node % (n+1)] != cost:
            continue
        for adj, w in edge_map[node]:
            if cost + w < dist[adj % (n+1)]:
                dist[adj % (n+1)] = cost + w
                heappush(heap, (cost+w, adj))
    return dist


def solve():
    n, m = mi()
    a, b = li(), li()

    edge_map = [[] for i in range(2*n+2)]
    for i in range(m):
        u, v, w = mi()
        edge_map[u].append((v, w))
        edge_map[v].append((u, w))
    for i in range(m):
        u, v, w = mi()
        u, v = u+n+1, v+n+1
        edge_map[u].append((v, w))
        edge_map[v].append((u, w))

    x, y = mi()
    dist1 = dijkstra(edge_map, x, n)
    dist2 = dijkstra(edge_map, y+n+1, n)

    ans = INF
    for i in range(1, n+1):
        for j in range(n+i, 2*n+1, i):
            w = a[i-1] * b[j-1-n]
            ans = min(ans, dist1[i] + dist2[j-n] + w)
            # edge_map[i].append((j, w))

    print(ans) if ans < INF else print(-1)
    # print(f"Dijkstra from {x} to {y}")


# test = 1
test = ii()
for _ in range(test):
    solve()
