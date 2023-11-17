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


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

def maxSubArray(nums) -> int:
    maxSum = float('-inf')
    currentSum = 0
    
    for num in nums:
        currentSum += num
        if currentSum > maxSum: maxSum = currentSum
        if currentSum < 0: currentSum = 0
    return maxSum

def solve():
    n = ii()
    arr = li()
    maxx = float('-inf')
    prev = 0
    for i in range(1, n):
        if arr[i]%2 == arr[i-1]%2:
            ans = maxSubArray(arr[prev:i])
            # print(prev, i, arr[prev:i], ans)
            maxx = max(maxx, ans)
            prev = i
    
    ans = maxSubArray(arr[prev:n])
    maxx = max(maxx, ans)
    # print(prev, n, arr[prev:n], ans)
    print(maxx)




# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
