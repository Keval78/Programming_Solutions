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


def calc(a, b, l, r):
    return abs(a[l]-b[r]) + abs(a[r]-b[l])

# DP with Moemoization.


def dp(memo, a, b, idx, k):
    if idx < 0 or idx >= len(a):
        return 0
    if k <= 0:
        return 0

    if memo[idx][k] != -1:
        return memo[idx][k]

    res = 0
    for l in range(1, k+1):
        res = max(res, dp(memo, a, b, idx - l, k - l) +
                  calc(a, b, idx - l + 1, idx))
    res = max(res, dp(memo, a, b, idx + 1, k))

    memo[idx][k] = res
    return res


def solve():
    n, k = mi()
    a, b = li(), li()
    memo = [[-1]*(k+2) for j in range(n)]
    res = dp(memo, a, b, 0, k)
    print(res)


# test = 1
test = ii()
for _ in range(test):
    solve()
    # break
