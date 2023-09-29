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
# from heapq import heapify, heappop, heappush, heapreplace
# from bisect import bisect_left, bisect_right


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 6)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


def distance_from_cycle(node, graph, cycle):
    visit = [False]*len(graph)
    que = [node]
    dis = 0
    while que:
        for i in range(len(que)):
            node = que.pop(0)
            if node == cycle:
                return dis

            visit[node] = True
            for adj in graph[node]:
                if not visit[adj]:
                    que.append(adj)
                    visit[adj] = True
        dis += 1


# def dfs_cycle(node, parent, graph, visit, path_visit, path):
#     """Graph DFS for Cycle check. Return True if node is in Cycle."""
#     # print(node)
#     visit[node] = path_visit[node] = True
#     path.append(node)

#     for adj in graph[node]:
#         if adj == parent:
#             continue
#         if not visit[adj]:
#             if dfs_cycle(adj, node, graph, visit, path_visit, path):
#                 return True
#         elif path_visit[adj]:
#             path.append(adj)
#             return True

#     path.pop()
#     path_visit[node] = False
#     return False


# def check_cycle_using_dfs(n, graph, a, b):
#     """Find Cycle in graph using DFS."""
#     visit = [False]*n
#     path_visit = [False]*n
#     path = []
#     dfs_cycle(b, -1, graph, visit, path_visit, path)

#     # print(len(path))
#     i = 0
#     while i < len(path) and path[i] != path[-1]:
#         i += 1

#     if b in path[i+1:]:
#         print("YES")
#     else:
#         # distance of cycle for connection b & a
#         db = distance_from_cycle(b, graph, path[i])
#         da = distance_from_cycle(a, graph, path[i])
#         # print("b, db, a, da", b, db, a, da)

#         if db < da:
#             print("YES")
#         else:
#             print("NO")


def check_cycle_iterative(node, graph):
    vis = [0 for i in range(len(graph))]
    c = 1
    q = deque([(node, -1)])
    while q:
        cur, par = q.pop()
        if vis[cur]:
            dis, loc = vis[cur], cur
            return dis, loc
        vis[cur] = c
        c += 1
        for adj in graph[cur]:
            if adj == par:
                continue
            q.append((adj, cur))


def solve():
    n, a, b = mi()
    a, b = a-1, b-1
    edge_map = defaultdict(list)
    for i in range(n):
        u, v = mi()
        edge_map[u-1].append(v-1)
        edge_map[v-1].append(u-1)

    if a == b:
        print("NO")
        return

    dis, loc = check_cycle_iterative(b, edge_map)
    # print(dis, loc)
    if dis == 1:  # Node b is in Cycle.
        print("YES")
        return

    # distance of cycle for connection b & a
    db = distance_from_cycle(b, edge_map, loc)
    da = distance_from_cycle(a, edge_map, loc)
    # print(da, db)
    if db < da:
        print("YES")
    else:
        print("NO")


# test = 1
test = ii()
for _ in range(test):
    solve()
