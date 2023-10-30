'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(32):
            j, bit = 0, 1 << i
            for num in nums:
                if num & bit:
                    j += 1
            if j >= k:
                ans += bit
        return ans
