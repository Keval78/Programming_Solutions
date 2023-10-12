'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

# import math
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
    n, m = mi()
    if m == 1:
        for i in range(n+1):
            print(0)
    else:
        if n >= m:
            print(m)
            for i in range(m-1):
                print(*[(j+i) % m for j in range(m)])
            for i in range(m, n+1):
                print(*[j for j in range(m)])
        else:
            print(n+1)
            for i in range(n):
                print(*[(j+i) % (n+1) if j <= n else j for j in range(m)])


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
