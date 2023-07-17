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

n = ii()
arr = li()
counts = [0 for i in range(5)]
total_taxi = 0

for num in arr:
    counts[num] += 1

total_taxi += counts[4]
total_taxi += counts[2]//2
total_taxi += min(counts[1], counts[3])  # Combine 3 and 1 group together
if counts[1] > counts[3]:
    total_taxi += (counts[1]-counts[3])//4
    if counts[2] % 2 != 0:
        if (counts[1]-counts[3]) % 4 < 3:
            total_taxi += 1
        elif (counts[1]-counts[3]) % 4 == 3:
            total_taxi += 2
    else:
        if (counts[1]-counts[3]) % 4 != 0:
            total_taxi += 1
else:
    total_taxi += (counts[3]-counts[1])
    if counts[2] % 2 != 0:
        total_taxi += 1

print(total_taxi)
