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
    n, m = mi()
    if n == 1 or m == 1:
        print("YES")
        continue
    if n % 2 == 0 or n <= m:
        print("NO")
        continue
    flag, i = True, 2
    while i*i <= n:
        if n % i == 0 and (i <= m or n//i <= m):
            flag, ans = False, "NO"
            break
        i += 1
    if (n % m == 0):
        flag, ans = False, "NO"
    if flag:
        ans = "YES"
    print(ans)
