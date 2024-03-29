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
        def thirdMax(self, nums: List[int]) -> int:
            nums.sort(reverse=True)
            uniq = 0
            last = nums[0]
            for i in range(len(nums)):
                if nums[i]!=last: uniq+=1
                last = nums[i]
                if uniq == 2: return nums[i]
            return nums[0]
    
    # Create Heap for Optimal Solution.
    Solution().thirdMax(nums = [3,2,1])


if __name__ == "__main__":
    main()
