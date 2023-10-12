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
    n, x = mi()
    arr = li()

    mh, sh = max(arr), sum(arr)

    def cal_water(h):
        if h > mh:
            ans = n*h-sh
        else:
            ans = 0
            for i in range(n):
                if arr[i] < h:
                    ans += h - arr[i]
        return ans

    l, r = 0, 10**11
    while l <= r:
        mid = (l+r)//2
        if cal_water(mid) <= x:
            l = mid+1
        else:
            r = mid-1

    if cal_water(l) <= x:
        print(l)
    else:
        print(r)


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
