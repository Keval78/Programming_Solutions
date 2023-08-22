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


def digitdp(memo, num: str, idx: int, tight: int):
    if idx == len(num):
        return 1

    # if memo[idx][non_zero][smaller] != -1:
    #     return memo[idx][non_zero][smaller]

    res = 0
    low, high = 0, int(num[idx]) if tight else 9
    for i in range(low, high+1):
        res += digitdp(memo, num, idx+1, 1 if tight and i ==
                       int(num[idx]) else 0)

    # memo[idx][non_zero][smaller] = res
    return res


def solve():
    l, r = mi()
    # print(l, r)
    # ANS -> [0, R] - [0, L-1]
    memo = [[-1]*2 for j in range(10)]
    right = digitdp(memo, str(r), 0, 1)
    # print(memo)
    print(right)


# test = 1
test = ii()
for _ in range(test):
    solve()
    break


# https://codeforces.com/contest/1036/problem/C
