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
    arr = li()

    idx = 0
    while idx < n:
        if arr[idx] >= 0:
            break
        idx += 2

    idx = min(idx, n)
    ans = 0
    for i in range(idx, n):
        if arr[i] > 0:
            ans += arr[i]

    if len(arr[:idx]) == 0:
        print(ans)
        return

    # print(idx)
    # print(arr)
    prefix = [0]*(idx)
    for i in range(idx-1, 0, -1):
        if arr[i] > 0:
            prefix[i-1] += arr[i]
        prefix[i-1] += prefix[i]

    maxi = 0
    for i in range(idx):
        if i % 2:
            maxi = max(maxi, prefix[i])
        else:
            maxi = max(maxi, arr[i]+prefix[i])

    # print("max", maxi)
    print(maxi+ans)


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
