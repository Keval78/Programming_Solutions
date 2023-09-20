"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nnums = []
        for i, num in enumerate(nums):
            nnums.append((num, i))
        nnums.sort()
        i, j = 0, len(nums)-1
        while i <= j:
            if target < nnums[i][0] + nnums[j][0]:
                j -= 1
            elif target > nnums[i][0] + nnums[j][0]:
                i += 1
            else:
                return [nnums[i][1], nnums[j][1]]
