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

for _ in range(ii()):
    n = ii()
    arr = li()

    visit = [i for i in range(n+1)]
    last = 0
    err = -1

    for i in range(n-1):
        val = arr[i] - last
        # print(val)
        if val > n or visit[val] == 0:
            if err != -1:
                print("NO")
                break
            else:
                err = val
        if val <= n:
            visit[val] = 0
        last = arr[i]
    else:
        cnt = 0
        for i in range(1, n+1):
            if visit[i] != 0:
                cnt += 1
        if (cnt == 1 and err == -1) or (cnt == 2 and sum(visit) == err):
            print("YES")
        else:
            print("NO")
