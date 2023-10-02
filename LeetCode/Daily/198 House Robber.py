'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = list(nums)
        n = len(nums)
        if n == 1:
            return nums[0]
        dp[1] = max(dp[0], dp[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + dp[i])
        return dp[-1]
