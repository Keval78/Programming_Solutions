'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cntr = Counter(nums)
        return True if max(cntr.values()) < 3 else False