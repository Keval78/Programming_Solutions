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
    n, k, one, two = mi()

    fancy = 0

    # n = y*k + x

    x = n % k
    if x > one:
        fancy += x-one
        one = 0
    else:
        one -= x
    # Convert remanining onw rupees coin into k rupees coin
    one //= k

    # y ?
    y = n//k
    if y > (two+one):
        fancy += y - (two+one)

    print(fancy)


# test = 1
test = ii()
for _ in range(test):
    solve()