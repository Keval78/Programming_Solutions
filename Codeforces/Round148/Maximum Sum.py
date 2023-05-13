from __future__ import division, print_function
from cmath import inf

import os
import sys
import math
from re import L
from io import BytesIO, IOBase
from collections import defaultdict


def ii(): return int(input())
def si(): return input()
def mi(ss=" "): return map(int, input().strip().split(ss))
def msi(ss=" "): return map(str, input().strip().split(ss))
def li(ss=" "): return list(mi(ss))


def read():
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')


def main():
    for _ in range(ii()):
        N, k = mi()
        arr = li()

        arr.sort()
        # left, right = 0, N-1

        S = sum(arr[0: len(arr) - k])
        ans = S
        for i in range(k):
            # if arr[left] + arr[left+1] > arr[right]:
            #     right -= 1
            # else:
            #     left += 2
            # print(sum(arr[left:right+1]), left, right+1)

            S -= arr[2 * i] + arr[2 * i + 1]
            S += arr[len(arr) - k + i]
            ans = max(ans, S)
        print(ans)
    return


if __name__ == "__main__":
    # read()
    main()
