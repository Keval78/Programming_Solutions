"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        j, mini = 0, float('inf')
        for i, num in enumerate(nums):
            if mini > num:
                mini = num
                j = i

        i, n = j, len(nums)
        while i % n != (j-1) % n:
            if nums[i % n] > nums[(i+1) % n]:
                return -1
            i += 1

        return j if j == 0 else n-j
