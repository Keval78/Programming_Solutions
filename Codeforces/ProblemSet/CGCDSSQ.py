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


# sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

n = ii()
arr = li()

results = {}
divisors, nextDivisors = {}, {}
for i in range(n):
    nextDivisors.clear()
    for p, count in divisors.items():
        next_gcd = math.gcd(p, arr[i])
        nextDivisors[next_gcd] = nextDivisors.get(next_gcd, 0) + count
    nextDivisors[arr[i]] = nextDivisors.get(arr[i], 0) + 1

divisors, nextDivisors = nextDivisors, divisors
for p, count in divisors.items():
    results[p] = results.get(p, 0) + count

q = int(input())
for _ in range(q):
    x = int(input())
    print(results.get(x, 0))
