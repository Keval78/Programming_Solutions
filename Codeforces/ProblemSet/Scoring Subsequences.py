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


def binary_seach(low, high, arr):
    n = high+1
    while low <= high:
        mid = (low + high)//2
        if arr[mid]/(n-mid) == 1:
            return mid
        elif arr[mid]/(n-mid) < 1:
            low = mid+1
        else:
            high = mid-1
    # print(low)
    return low


for _ in range(ii()):
    n = ii()
    arr = li()
    for i in range(0, n):
        ind = binary_seach(0, i, arr)
        print(i+1-ind, end=" ")
    print()
