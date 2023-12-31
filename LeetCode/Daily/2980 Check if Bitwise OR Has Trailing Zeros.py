'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return True if sum([1 for num in nums if num & 1 == 0]) > 1 else False