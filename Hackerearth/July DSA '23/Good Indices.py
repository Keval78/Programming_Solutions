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

for _ in range(ii()):
    n = ii()
    arr = li()
    # print(arr)
    left = [-1 for i in range(n)]
    right = [-1 for i in range(n)]
    preq, sufq = deque(), deque()
    preq.append((-1, -1))
    sufq.append((-1, -1))

    for i in range(1, n-1):
        if arr[i-1] < arr[i]:
            preq.append((arr[i-1], i-1))
        else:
            while preq[-1][0] >= arr[i]:
                preq.pop()
        left[i] = preq[-1][1]

        if arr[n-i] < arr[n-i-1]:
            sufq.append((arr[n-i], n-i))
        else:
            while sufq[-1][0] >= arr[n-i-1]:
                sufq.pop()
        right[n-i-1] = sufq[-1][1]

    # print(left)
    # print(right)
    for i in range(n-1):
        if left[i] == -1 or right[i] == -1:
            print(-1, end=" ")
        else:
            print(right[i]-left[i]-2, end=" ")
    print(-1)
