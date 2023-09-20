"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List, Optional


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 2:
            return -1
        nums.sort()
        l, r = 0, n-1
        ans = -1
        while l < r:
            print(l, r, nums[l] + nums[r])
            if k > nums[l] + nums[r]:
                ans = max(ans, nums[l] + nums[r])
                l += 1
            else:
                r -= 1

        return ans
