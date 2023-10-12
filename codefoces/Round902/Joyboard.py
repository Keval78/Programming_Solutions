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


def solve():
    n, p = li()
    arr = li()
    brr = li()

    powers = [(i, j) for i, j in zip(brr, arr)]
    powers.sort()

    remain, used = n-1, p
    for power, cnt in powers:
        if power >= p:
            break
        if cnt > 0:
            if cnt <= remain:
                remain -= cnt
                used += power*cnt
            else:
                used += remain*power
                remain = 0
    if remain > 0:
        used += remain*p
        remain = 0
    print(used)


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
