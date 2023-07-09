'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import sys
from os import path
from math import log2, floor, ceil, sqrt, pow, gcd
import math
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
MOD, MOD2, INF, MAX = 10 ** 9 + 7, 998244353, float('inf'), 10**22

#           3,      4,      5,      6,      7,      8,      9,      10, ....... ,
# k = 2
# k = 3
# k = 4
# k = 5
# .
# .
# k =


def binpow(a: int, b: int) -> int:
    res = 1
    n = b
    while (b > 0):
        if (b & 1) == 1:
            res = res*a
        a = a*a
        b >>= 1
    return res


def array(k, n):
    return (binpow(k, n)-1)//(k-1)


def binary_search(n, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        mid_val = array(mid, n)
        # print(mid_val)
        if mid_val == x:
            return True
        elif mid_val > x:
            return binary_search(n, low, mid - 1, x)
        else:
            return binary_search(n, mid + 1, high, x)
    else:
        return False


for i in range(ii()):
    val = ii()
    for n in range(3, 80):
        low = 2
        high = max(2, int((10**18)**(1/(n-1))))
        if binary_search(n, low, high, val):
            print("YES")
            break
    else:
        print("NO")
