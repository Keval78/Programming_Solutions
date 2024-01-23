'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        total = maxf = 0
        for key, val in cntr.items():
            if val >= maxf:
                if val > maxf: total = 0
                maxf = val
                total += val

        return total