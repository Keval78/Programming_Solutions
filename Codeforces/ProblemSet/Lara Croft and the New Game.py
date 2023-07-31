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


n, m, k = mi()

if k < n:
    print(1+k, 1)
elif k < (n+m-1):
    print(n, k-n+2)
else:
    k -= (n+m-2)
    m -= 1
    row = n - k//m
    if (k % m) != 0:
        row -= 1
        if row % 2 == 1:  # Decreasing...
            col = m+2 - k % m
        else:
            col = 1 + k % m
    else:
        if row % 2 == 1:  # Decreasing...
            col = 2
        else:
            col = m+1
    print(row, col)
