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
    n, k = mi()
    def binary_search(low, high, n, k):
        if high >= low:
            mid = (high+low)//2
            if mid-(mid//n) == k:
                return mid-1 if mid%n==0 else mid
            elif mid-(mid//n) > k:
                return binary_search(low, mid-1, n, k)
            else:
                return binary_search(mid+1, high, n, k)
        else:
            return False
    
    val = binary_search(0, n*k, n, k)
    print(val)
    
    
    