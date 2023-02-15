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
        def validWordAbbreviation(self, word: str, abbr: str) -> bool:
            wp = ap = 0
            while wp<len(word) and ap<len(abbr):
                if abbr[ap].isdigit():
                    steps = 0
                    if abbr[ap] == '0': return False
                    while ap<len(abbr) and abbr[ap].isdigit():
                        steps = steps*10 + int(abbr[ap])
                        ap += 1
                    
                    wp += steps
                else:
                    if word[wp] != abbr[ap]: return False
                    wp , ap = wp+1, ap+1
            return wp == len(word) and ap == len(abbr)
    
    Solution().validWordAbbreviation(word = "internationalization", abbr = "i12iz4n")


if __name__ == "__main__":
    main()
