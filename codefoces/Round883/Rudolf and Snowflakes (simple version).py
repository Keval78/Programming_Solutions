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
MAX = 10 ** 6


def binpow(a: int, b: int) -> int:
    res = 1
    while (b > 0):
        if (b & 1) == 1:
            res = res*a
        a = a*a
        b >>= 1
    return res


def array(k, n):
    return (binpow(k, n)-1)//(k-1)


def find_case(val):
    k = 2
    while True:
        temp = array(k, 3)
        if temp > val:
            break
        # arr.append([temp])
        if val == temp:
            return True
        n = 4
        while True:
            temp = array(k, n)
            if temp > val:
                break
            if val == temp:
                return True
            n += 1
        k += 1
    return False


for _ in range(ii()):
    val = ii()
    if find_case(val):
        print("YES")
    else:
        print("NO")
