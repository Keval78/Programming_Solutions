'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from functools import cache

class Solution:
    def maxOperations2(self, nums: List[int]) -> int:
        # DP with memoization

        def topdowndp(start, end, target, memo):
            # base condition
            if start < 0 or end >= n or start >= end:
                return 0
            
            if memo[start][end] != 0:
                return memo[start][end]
            
            res = 0
            if start<n-1 and (not target or nums[start] + nums[start+1] == target):
                res = max( 
                    res, 
                    1 + topdowndp(start+2, end, nums[start] + nums[start+1], memo)
                )
            
            if end>0 and (not target or nums[end] + nums[end-1] == target):
                res = max( 
                    res, 
                    1 + topdowndp(start, end-2, nums[end] + nums[end-1], memo)
                )
            
            if end>=0 and start<n and (not target or nums[start] + nums[end] == target):
                res = max( 
                    res, 
                    1 + topdowndp(start+1, end-1, nums[start] + nums[end], memo)
                )
            memo[start][end] = res
            
            return res

        n = len(nums)
        memo = [[0]*n for i in range(n)]
        return topdowndp(0, n-1, None, memo)
    

    def maxOperations(self, nums: List[int]) -> int:
        # DP with memoization
        if all([i == nums[0] for i in nums]):
            return len(nums) >> 1

        @cache
        def topdowndp(start, end, target):
            # base condition
            if start >= end: return 0
            
            res = 0
            if nums[start] + nums[start+1] == target:
                res = max(res, 1 + topdowndp(start+2, end, target))
            
            if nums[end] + nums[end-1] == target:
                res = max(res, 1 + topdowndp(start, end-2, target))
            
            if nums[start] + nums[end] == target:
                res = max( res, 1 + topdowndp(start+1, end-1, target))
            
            return res

        n = len(nums)
        return max(
            topdowndp(0, n-1, nums[0] + nums[1]),
            topdowndp(0, n-1, nums[0] + nums[-1]),
            topdowndp(0, n-1, nums[-1] + nums[-2])
        )

nums = [3,2,1,2,3,4]
ans = Solution().maxOperations(nums)
print(ans)

nums = [3,2,6,1,4]
ans = Solution().maxOperations(nums)
print(ans)