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
from itertools import permutations, combinations
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


# def dijkstra(arr, majors, src, dest):
#     heap = [(0, src)]
#     costs = [INF for _ in range(len(arr)+1)]
#     visited = set()

#     while heap:
#         print(heap)
#         cost, node = heappop(heap)
#         if node in visited:
#             continue
#         costs[node] = cost
#         visited.add(node)

#         if node == dest:
#             return cost

#         for adj_idx, adj in enumerate(arr):
#             if adj_idx in visited:
#                 continue

#             x, y = arr[node]
#             if node < majors and adj_idx < majors:
#                 if cost < costs[adj_idx]:
#                     heappush(heap, (cost, adj_idx))
#                     costs[adj_idx] = cost

#             else:
#                 dist = abs(x-adj[0]) + abs(y-adj[1])
#                 if cost + dist < costs[adj_idx]:
#                     heappush(heap, (cost + dist, adj_idx))
#                     costs[adj_idx] = cost + dist

#     return -1

def distance(a, b, arr):
    return abs(arr[b][0]-arr[a][0]) + abs(arr[b][1]-arr[a][1])


def solve():
    n, k, source, dest = mi()
    arr = []
    for i in range(n):
        x, y = mi()
        arr.append((x, y))
    if source <= k and dest <= k:
        print(0)
    else:
        cost = distance(source-1, dest-1, arr)
        cost1 = cost2 = INF
        for i in range(k):
            cost1 = min(cost1, distance(source-1, i, arr))
            cost2 = min(cost2, distance(i, dest-1, arr))
        cost = min(cost, cost1 + cost2)
        print(cost)


# test = 1
test = ii()
for _ in range(test):
    solve()
