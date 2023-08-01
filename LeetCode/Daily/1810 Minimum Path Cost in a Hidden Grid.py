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
from heapq import heapify, heappop, heappush, heapreplace
from bisect import bisect_left, bisect_right
from typing import List


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

# PYTHON Intrective code...


grid = [[0, 3, 1], [3, 4, 2], [1, 2, 0]],
start = [2, 0]
target = [0, 2]


def canMove(x, y, direction: str) -> bool:

    if x, y =


def findShortestPath(master: 'GridMaster'):
    max_n, max_m = 10, 10
    visit = [[0 for i in range(max_n)] for j in range(max_m)]
    i, j = max_n//2, max_m//2

    print(visit)


tasks = [[1, 3], [1, 2], [2, 4], [3, 2], [4, 1]]
getOrder(tasks)
