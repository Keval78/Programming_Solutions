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
from operator import itemgetter


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

for _ in range(ii()):
    n = ii()
    arr = li()

    # count = Counter(arr)
    # print(count)
    count = [0 for i in range(n+1)]
    for i in range(n):
        if arr[i] <= n:
            count[arr[i]] += 1

    max_frogs = 0
    for i in range(1, n+1):
        curr_frogs = 0
        j = 1
        while j <= sqrt(i):
            if (i % j) == 0:
                curr_frogs += count[j]
                if (i//j != j):
                    curr_frogs += count[i//j]
            j += 1
        max_frogs = max(max_frogs, curr_frogs)

    print(max_frogs)
