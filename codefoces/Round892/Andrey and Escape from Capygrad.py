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
# from heapq import heapify, heappop, heappush, heapreplace
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
    n = ii()
    segments = []
    for i in range(n):
        seg = li()
        segments.append([seg[0], seg[-1]])
    segments.sort()

    sgmnts = []
    start, end = segments[0][0], segments[0][1]
    for i in range(1, n):
        if segments[i][0] <= end:
            end = max(end, segments[i][1])
        else:
            sgmnts.append([start, end])
            start, end = segments[i][0], segments[i][1]
    sgmnts.append([start, end])
    # print(sgmnts)

    nn = len(sgmnts)
    q = ii()
    queries = li()
    for i in range(q):
        x = queries[i]
        l, r = 0, nn-1
        while l <= r:
            mid = (l+r)//2
            if sgmnts[mid][0] <= x <= sgmnts[mid][1]:
                queries[i] = sgmnts[mid][1]
                break
            elif sgmnts[mid][0] > x:
                r = mid - 1
            else:
                l = mid + 1
    print(*queries)


# test = 1
test = ii()
for _ in range(test):
    solve()
