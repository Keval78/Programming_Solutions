'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                distinct = len(set(nums[i:j+1]))
                ans += distinct**2
        return ans


nums = [1, 2, 1]
ans = Solution().sumCounts(nums)
print(ans)
