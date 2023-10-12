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

n, m = mi()
cnt = 0
min_r, max_r, min_c, max_c = n, 0, m, 0
for i in range(n):
    s = si()
    for j in range(m):
        if s[j] == "B":
            cnt += 1
            min_c = min(min_c, j)
            max_c = max(max_c, j)

            min_r = min(min_r, i)
            max_r = max(max_r, i)

length = max(max_c-min_c+1, max_r-min_r+1)
if length > n or length > m:
    print("-1")
elif length <= 0:
    print("1")
else:
    print(length*length - cnt)
