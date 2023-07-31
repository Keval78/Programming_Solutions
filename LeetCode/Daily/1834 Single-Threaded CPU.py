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


def getOrder(tasks: List[List[int]]) -> List[int]:
    # Added index for the equal processing time.
    for i, task in enumerate(tasks):
        task.append(i)
    tasks.sort(key=lambda t: t[0])

    ans, task_heap = [], []
    ind, curr_time = 0, 0
    while task_heap or ind < len(tasks):
        if not task_heap:
            curr_time = max(curr_time, tasks[ind][0])
            # print(curr_time)

        while ind < len(tasks) and tasks[ind][0] <= curr_time:
            heappush(task_heap, [tasks[ind][1], tasks[ind][2]])
            ind += 1
        # print(task_heap, curr_time)
        proc_time, curr_ind = heappop(task_heap)
        curr_time += proc_time
        ans.append(curr_ind)
        # print(curr_time)
    print(ans)


tasks = [[1, 3], [1, 2], [2, 4], [3, 2], [4, 1]]
getOrder(tasks)
