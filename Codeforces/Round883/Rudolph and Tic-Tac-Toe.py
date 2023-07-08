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


def sign_and(sign1, sign2, sing3):
    if sign1 != "." and sign1 == sign2 == sing3:
        return sign1
    return "DRAW"


def sign_or(sign1, sign2):
    if sign1 != "DRAW":
        return sign1
    elif sign2 != "DRAW":
        return sign2
    else:
        return "DRAW"


for _ in range(ii()):
    board = [si() for i in range(3)]
    ans = "DRAW"

    for i in range(3):
        raw_winner = sign_and(board[i][0], board[i][1], board[i][2])
        # print("raw", i, raw_winner)
        ans = sign_or(ans, raw_winner)
        # print(ans)

        col_winner = sign_and(board[0][i], board[1][i], board[2][i])
        # print("col", i, col_winner)
        ans = sign_or(ans, col_winner)
        # print(ans)
    ans = sign_or(ans, sign_and(board[0][0], board[1][1], board[2][2]))
    ans = sign_or(ans, sign_and(board[0][2], board[1][1], board[2][0]))
    print(ans)
