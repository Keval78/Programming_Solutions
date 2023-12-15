'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import sys
# from os import path
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
MAX = 10**5+1


def solve():
    n = ii()
    arr = li()

    # ai - log(ai) = aj - log(aj)
    uniq_vals = defaultdict(int)

    for i in range(n):
        val = arr[i] - log2(arr[i])
        uniq_vals[val] += 1
    
    total = 0
    for k, val in uniq_vals.items():
        if val > 1:
            total += (val*(val-1))//2
    print(total)



# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
