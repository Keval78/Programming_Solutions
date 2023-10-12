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
    n, k = mi()
    arr = li()
    heights = li()

    subs = []
    i = 1
    curr = [arr[0]]
    while i < n:
        if heights[i-1] % heights[i] == 0:
            curr.append(arr[i])
        else:
            subs.append(curr)
            curr = [arr[i]]
        i += 1
    subs.append(curr)

    ans = 0
    for sub in subs:
        l, r = 0, 0
        total = 0
        while l < len(sub) and r < len(sub):
            if total + sub[r] <= k:
                total += sub[r]
                r += 1
            else:
                total -= sub[l]
                l += 1
            ans = max(ans, r-l)

    print(ans)


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
