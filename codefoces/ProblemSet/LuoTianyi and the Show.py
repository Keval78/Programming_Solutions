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


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


def solve():
    n, m = mi()
    arr = li()

    left, right = 0, 0
    fixed = set()
    for i in range(n):
        if arr[i] == -1:
            left += 1
        elif arr[i] == -2:
            right += 1
        else:
            fixed.add(arr[i])

    # print(len(fixed))
    lf = 0
    # print(0, right+rf)
    res = right+len(fixed)
    for pos in sorted(fixed):
        rf = len(fixed)-lf-1
        ans = 1 + min(pos-1, left+lf) + min(m-pos, right+rf)
        # print(pos, ans)
        res = max(res, ans)
        lf += 1
    # print(n, left+lf)
    res = max(res, left+lf)
    res = min(res, m)
    print(res)


# test = 1
test = ii()
for _ in range(test):
    solve()
