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
        def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        # val = arr[0]
        # inc = True
        # for i in range(1,len(arr)):
        #     if (inc and arr[i] > val) or (not inc and arr[i] < val): val = arr[i]
        #     else:
        #         if inc and i!=1 and arr[i] < val: val, inc = arr[i], False
        #         else: return False
        # return not inc

        i=0
        # walk up
        while(i<len(arr)-1 and arr[i]<arr[i+1]): i+=1
        
        # peak can't be first or last
        if i==0 or i==len(arr)-1: return False

        #walk down    
        while(i<len(arr)-1 and arr[i]>arr[i+1]): i+=1

        return i == len(arr)-1
    
    Solution().validMountainArray(arr = [3,5,5])


if __name__ == "__main__":
    main()
