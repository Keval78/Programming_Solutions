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

# DP with Moemoization.
def digitdp(memo, num: str, idx: int, non_zero: int, smaller: int):
    # Number of nonzero digit <= 3
    if non_zero > 3:
        return 0

    if idx == len(num):
        return 1

    if memo[idx][non_zero][smaller] != -1:
        return memo[idx][non_zero][smaller]

    # If it is smaller.
    res = digitdp(memo, num, idx+1, non_zero,
                  smaller if smaller else 1 if num[idx] != "0" else 0)
    if smaller:
        res += 9*digitdp(memo, num, idx+1, non_zero+1, 1)
    else:
        lesser = int(num[idx]) - 1
        if lesser > 0:
            res += lesser*digitdp(memo, num, idx+1, non_zero+1, 1)
        if num[idx] != "0":
            res += digitdp(memo, num, idx+1, non_zero+1, 0)

    memo[idx][non_zero][smaller] = res
    return res


def solve():
    l, r = mi()
    # print(l, r)
    # ANS -> [0, R] - [0, L-1]
    memo = [[[-1]*2 for i in range(4)] for j in range(20)]
    right = digitdp(memo, str(r), 0, 0, 0)

    memo = [[[-1]*2 for i in range(4)] for j in range(20)]
    left = digitdp(memo, str(l-1), 0, 0, 0)
    # print(memo)
    print(right - left)


# test = 1
test = ii()
for _ in range(test):
    solve()


# https://codeforces.com/contest/1036/problem/C
