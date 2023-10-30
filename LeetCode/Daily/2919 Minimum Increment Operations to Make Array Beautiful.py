'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
INF = float('inf')


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # DP with memoization

        def topdowndp(idx, prev, memo):
            if idx == n:
                return 0

            if memo[idx][prev] != -1:
                return memo[idx][prev]

            res = INF
            if nums[idx] < k:
                res = min(res, k-nums[idx] + topdowndp(idx+1, 0, memo))
                if prev < 2:
                    res = min(res, topdowndp(idx+1, prev+1, memo))
            else:
                res = min(res, topdowndp(idx+1, 0, memo))

            memo[idx][prev] = res
            return res

        memo = [[-1]*3 for i in range(n)]
        ans = topdowndp(0, 0, memo)
        return ans


nums = [2, 3, 0, 0, 2]
k = 4
ans = Solution().minIncrementOperations(nums, k)
print(ans)

nums = [0, 1, 3, 3]
k = 5
ans = Solution().minIncrementOperations(nums, k)
print(ans)

nums = [1, 1, 2]
k = 1
ans = Solution().minIncrementOperations(nums, k)
print(ans)
