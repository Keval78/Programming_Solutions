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


# sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

for _ in range(ii()):
    n, k = mi()
    arr = li()

    if k==1:
        print("0")
        continue
    freq = [[] for i in range(n+1)]
    for i in range(n):
        freq[arr[i]].append(i+1)
    
    min_step = INF
    for planks in freq:
        max_steps = []
        prev = 0
        for plank in planks:
            max_steps.append(plank-prev-1)
            max_steps.sort(reverse=True)
            max_steps = max_steps[:3]
            prev = plank
        if prev != 0:
            max_steps.append(n-prev)
            max_steps.sort(reverse=True)
            max_steps = max_steps[:3]
        
        if max_steps:
            max_steps[0] = max_steps[0]//2
            min_step = min(min_step, max(max_steps))
    print(min_step)

