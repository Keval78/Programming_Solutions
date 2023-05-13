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
        N = ii()
        arr = li()

        mcount = 1
        increasing = 0
        for i in range(1, N):
            if (increasing == 1 and arr[i] - arr[i-1] < 0) or (increasing == -1 and arr[i] - arr[i-1] > 0):
                increasing = -1 * increasing
                mcount += 1
            if increasing == 0 and arr[i] - arr[i-1] > 0:
                increasing = 1
                mcount += 1
            if increasing == 0 and arr[i] - arr[i-1] < 0:
                increasing = -1
                mcount += 1
        print(mcount)
    return


if __name__ == "__main__":
    # read()
    main()
