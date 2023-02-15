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
        def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
            if (length>=10**4 or width>=10**4 or height>=10**4 or length*width*height>=10**9) and mass>=100: return "Both"
            if length>=10**4 or width>=10**4 or height>=10**4 or length*width*height>=10**9: return "Bulky"
            if mass>=100: return "Heavy"
            return "Neither"
    
    Solution().categorizeBox(length = 1000, width = 35, height = 700, mass = 300)


if __name__ == "__main__":
    main()
