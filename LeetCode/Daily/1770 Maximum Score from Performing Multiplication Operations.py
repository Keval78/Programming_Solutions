'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        # DP with memoization
        def topdowndp(idx, start, memo, nums, multipliers):
            if idx == len(multipliers):
                return 0
            if memo[idx][start] != -1:
                return memo[idx][start]
            res = max(
                nums[start]*multipliers[idx] +
                topdowndp(idx+1, start+1, memo, nums, multipliers),
                nums[len(nums)-1 + start - idx]*multipliers[idx] +
                topdowndp(idx+1, start, memo, nums, multipliers)
            )
            memo[idx][start] = res
            return res

        n = len(nums)
        memo = [[-1]*len(multipliers) for i in range(n)]
        ans = topdowndp(0, 0, memo, nums, multipliers)
        return ans
