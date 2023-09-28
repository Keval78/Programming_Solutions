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
    arr = []
    cnt = [0 for i in range(50)]

    for i in range(n):
        s = li()
        arr.append(s[1:])
        for i in range(1, len(s)):
            cnt[s[i]-1] += 1

    # print(arr)
    # print(cnt[:11])

    maxi = 0
    for i, c in enumerate(cnt):
        if c == 0:
            continue
        # union all which do not contain (i+1)
        union = [False]*51
        for l in arr:
            if (i+1) in l:
                continue
            for ele in l:
                union[ele] = True

        t = 0
        for i in union:
            if i:
                t += 1
        maxi = max(maxi, t)

    print(maxi)


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
