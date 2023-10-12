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

    # print(arr, pres, prem)
    idxs = []
    for i in range(n):
        if arr[i] != 1:
            idxs.append(i)

    if len(idxs) >= 20:
        print(min(idxs)+1, max(idxs)+1)
        return

    pres = [0] + list(arr)
    prem = [1] + list(arr)

    for i in range(n):
        pres[i+1] += pres[i]
        prem[i+1] *= prem[i]

    ans = 0
    lidx = ridx = 0
    m = len(idxs)
    for i in range(m):
        for j in range(i, m):
            # find value for range [l, r]
            l, r = idxs[i], idxs[j]
            # print(l, r)

            pre_sum = pres[l]
            curr = prem[r+1]//prem[l]
            post_sum = (pres[n]-pres[r+1])

            temp = pre_sum + curr + post_sum

            if ans < temp:
                ans = temp
                lidx, ridx = l, r

    print(lidx+1, ridx+1)


# test = 1
test = ii()
for _ in range(test):
    solve()
