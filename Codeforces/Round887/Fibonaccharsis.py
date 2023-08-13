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
# from bisect import bisect_left, bisect_right


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')

for _ in range(ii()):
    n, k = mi()
    flag = True
    x, y = 1, 1
    for i in range(k-3):
        x, y = y, x+y
        if y > n:
            flag = False
            break
    if (not flag):
        print(0)
    else:
        ans = 0
        i = 0
        while i*x <= n:
            if ((n-i*x) % y == 0 and i <= (n-i*x)/y):
                ans += 1
            i += 1
        print(ans)
