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

# PYTHON Interactive code / Interactive problem...


def input_str(check, val):
    if check <= val:
        return ">="
    else:
        return "<"


val = 10**6
l, r = 1, 10**6+1
while l < r:
    mid = (l+r)//2
    print(mid)
    sys.stdout.flush()
    # input_s = si()
    if input_str(mid, val) == ">=":
        l = mid+1
    else:
        r = mid
print("!", l-1)
sys.stdout.flush()
