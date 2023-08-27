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


def solve():
    n, m = mi()
    grid = [[0]*m for i in range(n)]
    for _ in range(ii()):
        try:
            i, j = mi()
        except:
            break
        grid[i][j] = -1

    # for g in grid:
    #     print(g)

    # Min. plant count for each row
    max_plants = min_plants = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if grid[i][j] == -1:
                if cnt != 0:
                    min_plants += (cnt+2)//3
                    max_plants += (cnt+1)//2
                    cnt = 0
            else:
                cnt += 1
        if cnt != 0:
            min_plants += (cnt+2)//3
            max_plants += (cnt+1)//2

    print(max_plants, min_plants)


test = 1
# test = ii()
for _ in range(test):
    solve()
