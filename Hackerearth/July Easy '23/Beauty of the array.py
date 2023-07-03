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

n, arr = ii(), li()
max_number = max(arr)+1  # 10**5+1
prime_factors = [[] for i in range(max_number+1)]

for p in range(2, max_number):
    if len(prime_factors[p]) == 0:
        prime_factors[p].append(p)
        for i in range(2*p, max_number+1, p):
            prime_factors[i].append(p)
# print(prime_factors)

freq_map = defaultdict(int)
for ele in arr:
    factors_tpl = tuple(prime_factors[ele])
    freq_map[factors_tpl] += 1

ans = 1
for val in freq_map.values():
    ans *= val
    ans %= MOD
print(ans)
