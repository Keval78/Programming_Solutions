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


def bruteforce(n, arr):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n+1):
            ans = 0
            for ele in arr[i:j]:
                ans |= ele
            # print(arr[i:j], Counter(bin(ans)))
            bits = Counter(bin(ans))
            if '1' in bits and bits['1'] % 2 == 1:
                cnt += 1
    return cnt


def or_count(n, arr):
    results = {}
    ors, nextOrs = {}, {}
    ans = 0

    for i in range(n):
        nextOrs.clear()
        for p, count in ors.items():
            next_or = p | arr[i]
            nextOrs[next_or] = nextOrs.get(next_or, 0) + count
        nextOrs[arr[i]] = nextOrs.get(arr[i], 0) + 1
        ors, nextOrs = nextOrs, ors

        for p, count in ors.items():
            bits = Counter(bin(p))
            if '1' in bits and bits['1'] % 2 == 1:
                ans += count
    return ans


def solve():
    n = ii()
    arr = li()

    # arr = [i for i in range(n)]
    # bfcnt = bruteforce(n, arr)
    # print(bfcnt)

    dict_cnt = or_count(n, arr)
    print(dict_cnt)

    # LOGIC:
    # Number of OR set bits = Number of total set bits - Number of AND set bits
    #                       = Number of XOR set bits + Number of AND set bits

    # ans = 0
    # cnt_even, cnt_odd = 1, 0
    # XOR = 0

    # for ele in arr:
    #     XOR ^= ele

    #     cnt = 0
    #     for b in range(32):
    #         cnt += ((1 << b) & XOR) > 0

    #     if cnt % 2 == 1:
    #         ans += cnt_even
    #         cnt_odd += 1
    #     else:
    #         ans += cnt_odd
    #         cnt_even += 1
    # print(ans)


# test = 1
test = ii()
for _ in range(test):
    solve()
