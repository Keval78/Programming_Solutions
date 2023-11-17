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


def solve():
    n = ii()
    arr = list(msi())

    cnt = [[[0]*6 for i in range(6)] for j in range (50)]
    # print(cnt)

    for num in arr:
        total = sum([int(i) for i in num])
        # print(total)
        length = len(num)
        for i in range(length+1):
            # print(total, length, i)
            cnt[total][length][i] += 1
            if i < length:
                total -= int(num[i]) + int(num[i])
            if total < 0: break
    
    pairs = {
        1: [1, 3, 5],
        3: [1, 3, 5],
        5: [1, 3, 5],
        2: [2, 4],
        4: [2, 4]
    }

    ans = 0
    for num in arr:
        length = len(num)
        for slen in pairs[length]:
            if length < slen:
                total = sum([int(i) for i in num])
                skip = (length+slen)//2 - length
                ans += cnt[total][slen][skip]
            elif slen < length:
                total = 0
                for i in range(length):
                    if i < (length + slen)//2:
                        total += int(num[i])
                    else:
                        total -= int(num[i])
                if total > 0:
                    ans += cnt[total][slen][0]
            else:
                total = sum([int(i) for i in num])
                ans += cnt[total][length][0]

    print(ans)







test = 1
# test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
