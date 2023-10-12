'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

# import math
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


def xor_sum(bit, n, arr):
    cnt_zero = cnt_one = sum_zero = sum_one = 0
    res = 0
    for i in range(n):
        if arr[i] & bit:
            # bit position is one in number.
            cnt_zero, cnt_one = cnt_one, cnt_zero
            sum_zero, sum_one = sum_one, sum_zero
            cnt_one += 1
        else:
            # bit position is zero in number.
            cnt_zero += 1
        sum_zero += cnt_zero
        sum_one += cnt_one
        # print(sum_one)
        res += sum_one
    # print(res)
    return (bit * res) % MOD2


def solve():
    n = ii()
    arr = li()

    ans = 0
    for i in range(32):
        bit = 1 << i
        ans += xor_sum(bit, n, arr)
        ans %= MOD2
    print(ans)


test = 1
# test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
