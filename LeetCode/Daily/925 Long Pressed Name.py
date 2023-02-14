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
            ni = 0       # index of name
            ti = 0       # index of typed
            while ni <= len(name) and ti < len(typed):
                if ni < len(name) and typed[ti] == name[ni]:
                    ti += 1
                    ni += 1
                elif typed[ti] == name[ni-1] and ni != 0:
                    ti += 1
                else:
                    return False
                
            return ni == len(name) and ti == len(typed)

    
    Solution()


if __name__ == "__main__":
    main()
