"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            nums[i] = (num, i)
        nums.sort()

        n = len(nums)
        prev_idx = 0
        ans = n
        for i, (num, idx) in enumerate(nums):
            if idx < prev_idx:
                ans += n-i 
            prev_idx = idx
        return ans