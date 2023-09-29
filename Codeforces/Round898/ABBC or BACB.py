'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

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
    s = si()
    n = len(s)

    all_chars = (s[0] == 'B' or s[n - 1] == 'B')

    for i in range(n - 1):
        if s[i] == s[i + 1] and s[i] == 'B':
            all_chars = True

    lens = []
    curr = 0
    for i in range(n):
        if s[i] == 'A':
            curr += 1
        else:
            if curr != 0:
                lens.append(curr)
            curr = 0

    if curr != 0:
        lens.append(curr)

    lens.sort()

    if not lens:
        print(0)
        return

    tot = 0
    if all_chars:
        tot += lens[0]
    for i in range(1, len(lens)):
        tot += lens[i]

    print(tot)


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
