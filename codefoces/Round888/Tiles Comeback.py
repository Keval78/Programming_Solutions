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


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


# Brute Force.
# def fun(k, ind, curr, cnt):
#     # print(k, ind, curr)
#     if k == 0 and ind == 0:
#         return True
#     ans = False
#     if k == 0:
#         for i in range(ind):
#             ans = ans or fun(cnt-1, i, arr[i], cnt)
#     else:
#         for i in range(ind):
#             if arr[i] == curr:
#                 ans = ans or fun(k-1, i, curr, cnt)
#     return ans


for _ in range(ii()):
    n, k = mi()
    arr = li()

    cnt = 0
    last = n-1
    for i in range(n):
        if arr[i] == arr[0]:
            cnt += 1
            if cnt == k:
                last = i

    if cnt < k:
        print("NO")
        continue
    else:
        if arr[n-1] == arr[0]:
            print("YES")
            continue
    cnt = 0
    for i in range(n-1, last-1, -1):
        if arr[i] == arr[n-1]:
            cnt += 1

    if cnt < k:
        print("NO")
    else:
        print("YES")
