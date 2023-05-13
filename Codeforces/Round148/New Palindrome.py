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
        s = si()
        s = s[:len(s)//2]
        if len(set(s)) >= 2:
            print("YES")
        else:
            print("NO")
    return


if __name__ == "__main__":
    main()
