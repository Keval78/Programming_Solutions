'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import sys
from os import path
from math import log2, floor, ceil, sqrt, pow, gcd
# from random import random, randint, shuffle, choice
from collections import Counter, defaultdict, deque
# from itertools import permutations, combinations
# from functools import reduce
# from heapq import heapify, heappop, heappush, heapreplace
from bisect import bisect_left, bisect_right
from operator import itemgetter


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

for _ in range(ii()):
    n, m = mi()
    s = si()

    pre_0 = [0 for i in range(n)]
    suf_1 = [0 for i in range(n)]

    p_0 = -1
    s_1 = n+1
    for i in range(n):
        if s[i] == "0":
            p_0 = i
        pre_0[i] = p_0

        if s[n-i-1] == "1":
            s_1 = n-i-1
        suf_1[n-i-1] = s_1

    # print(pre_0)
    # print(suf_1)

    ranges = {}
    for q in range(m):
        i, j = mi()
        x, y = max(i-1, suf_1[i-1]), min(j-1, pre_0[j-1])
        if y < x:
            ranges[(-1, -1)] = 1
        else:
            ranges[(x, y)] = 1
    print(len(ranges))
