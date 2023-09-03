"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(k, n+1):
            if len(set(nums[i-k:i])) >= m:
                ans = max(ans, sum(nums[i-k:i]))
        return ans
