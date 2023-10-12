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

n = ii()

live = [0 for i in range(n)]
dead = [0 for i in range(n)]
for i in range(n):
    live[i], dead[i] = mi()
    # dead[i] += 1
live.sort()
dead.sort()

max_living, year = -1, 0
i, j = 0, 0
# Two pointer Appraoch
curr_year = live[0]
curr_living = 0
while i < n and j < n:
    curr_year = min(live[i], dead[j])
    while i < n and live[i] == curr_year:
        i += 1
        curr_living += 1
    while j < n and dead[j] == curr_year:
        j += 1
        curr_living -= 1
    if max_living < curr_living:
        max_living = curr_living
        year = curr_year
    # print(i, j, curr_living, curr_year)

print(year, max_living)
