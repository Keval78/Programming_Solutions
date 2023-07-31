'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import sys
# from os import path
from math import log2, floor, ceil, sqrt, pow, gcd
# from random import random, randint, shuffle, choice
# from collections import Counter, defaultdict, deque
# from itertools import permutations, combinations
# from functools import reduce
# from heapq import heapify, heappop, heappush, heapreplace
from bisect import bisect_left, bisect_right
from typing import List


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


def equalizeWater(buckets: List[int], loss: int) -> float:
    buckets.sort()
    n = len(buckets)
    pref = [0 for i in range(n+1)]
    for i in range(n):
        pref[i+1] = pref[i] + buckets[i]

    def canFill(target):
        # print(target)
        ind = bisect_right(buckets, target)
        out = (pref[n]-pref[ind] - target*(n-ind))*(100-loss)
        need = (target*ind - pref[ind])*100
        if out >= need:
            return True
        else:
            return False

    kErr = 1e-5
    l, r = 0, max(buckets)
    while r - l > kErr:
        m = (l + r) / 2
        if canFill(m):
            l = m
        else:
            r = m
    print(l)


equalizeWater(li(), ii())
