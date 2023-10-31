'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
INF = float('inf')


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        # DP with memoization
        def topdowndp(idx, target):
            if target == 0:
                return 0

            if idx >= n or nums[idx] > target:
                return -INF

            if memo[idx][target] != -1:
                return memo[idx][target]

            res = max(1 + topdowndp(idx+1, target -
                      nums[idx]), topdowndp(idx+1, target))
            memo[idx][target] = res
            return res

        memo = [[-1]*1002 for i in range(n)]
        ans = topdowndp(0, target)
        return ans if ans > 0 else -1


nums = [1, 2, 3, 4, 5]
target = 9
ans = Solution().lengthOfLongestSubsequence(nums, target)
print(ans)

nums = [4, 1, 3, 2, 1, 5]
target = 7
ans = Solution().lengthOfLongestSubsequence(nums, target)
print(ans)

nums = [1, 1, 5, 4, 5]
target = 3
ans = Solution().lengthOfLongestSubsequence(nums, target)
print(ans)
