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


def fact(n):
    # initialize numerator and denominator
    ans = 1
    while n:
        ans *= n
        ans %= MOD2
        n -= 1
    return ans


def solve():
    s = si()
    n = len(s)
    cnts = []
    cnt = 1
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt += 1
        else:
            cnts.append(cnt)
            cnt = 1
    cnts.append(cnt)
    # Combination which one delete and then order to delete elements.
    ans = 1
    delete = 0
    for cnt in cnts:
        ans *= cnt
        ans %= MOD2
        delete += cnt-1

    res = (ans * fact(delete)) % MOD2
    print(delete, res)


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
