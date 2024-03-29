'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

#import collections
from collections import Counter, defaultdict

# import maths functions & constants
from math import gcd
from cmath import inf

# import functools.
from functools import reduce

# import Generic Type
from typing import Generic, TypeVar


def ii():  return int(input())
def si():  return input()
def mi(ss=" "):  return map(int,input().strip().split(ss))
def msi(ss=" "): return map(str,input().strip().split(ss))
def li(ss=" "):  return list(mi(ss))


def main():
    class Solution:
        def isLongPressedName(self, name: str, typed: str) -> bool:
            np, tp = 0, 0
            while np<=len(name) and tp<len(typed):
                if np < len(name) and name[np] == typed[tp]: np, tp = np + 1, tp + 1
                elif np!=0 and typed[tp]==name[np-1]: tp = tp + 1
                else: return False
            return np==len(name) and tp==len(typed)
    Solution()


if __name__ == "__main__":
    main()
