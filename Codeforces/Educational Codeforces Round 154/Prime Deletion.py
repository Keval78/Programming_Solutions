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


def issubsequence(s1, s2):
    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1
    return i == n


def solve():
    start, end = 2, 10000
    sieve = [True] * (end + 1)
    out = []
    for p in range(start, end + 1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, end + 1, p):
                sieve[i] = False

    # print(out)
    inp = si()

    for val in out:
        if val > 10 and issubsequence(str(val), inp):
            print(str(val))
            break


# test = 1
test = ii()
for _ in range(test):
    solve()
