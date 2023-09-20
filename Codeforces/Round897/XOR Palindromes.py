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
    n = ii()
    arr = si()

    mismatch = 0
    for i in range(n//2):
        # print(i, n-i-1, arr)
        if arr[i] != arr[n-i-1]:
            mismatch += 1

    if n % 2:
        print(mismatch*"0" + "1"*(n-2*mismatch+1) + mismatch*"0")
    else:
        print(mismatch*"0" + "10"*((n-2*mismatch)//2) + "1" + mismatch*"0")


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
