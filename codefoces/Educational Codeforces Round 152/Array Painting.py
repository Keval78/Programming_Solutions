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

n = ii()
arr = li()
uniq = []


i = 0
prev = arr[0]
for i in range(1, n):
    if arr[i] == 0:
        uniq.append(prev)
        prev = 0
    else:
        if prev == 0:
            uniq.append(prev)
        prev = max(prev, arr[i])
uniq.append(prev)

# print(uniq)
n = len(uniq)
count = 0
for i, num in enumerate(uniq):
    if num > 0:
        count += 1
    else:
        if i > 0 and uniq[i-1] > 0:
            uniq[i-1] -= 1
            continue
        if i < n-1 and uniq[i+1] > 0:
            uniq[i+1] -= 1
            continue
        count += 1
print(count)
