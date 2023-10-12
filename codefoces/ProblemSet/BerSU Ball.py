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

n = ii()
brr = li()
m = ii()
grr = li()

brr.sort()
grr.sort()

# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if brr[i] == grr[j] or brr[i]+1 == grr[j] or brr[i]-1 == grr[j]:
#             cnt += 1
#             grr[j] = -2
#             break
# print(cnt)

pairs = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n):
    for j in range(m):
        pairs[i+1][j+1] = pairs[i][j]
        if abs(brr[i]-grr[j]) <= 1:
            pairs[i+1][j+1] += 1
        pairs[i+1][j+1] = max(pairs[i+1][j+1], pairs[i][j+1], pairs[i+1][j])
print(pairs[n][m])
