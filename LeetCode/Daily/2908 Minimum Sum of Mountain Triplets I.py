'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_min = nums[0]
        ans = [float('inf')]*(n-2)
        for i in range(1, n-1):
            if left_min < nums[i]:
                ans[i-1] = left_min + nums[i]
            left_min = min(left_min, nums[i])

        right_min = nums[-1]
        for i in range(n-2, 0, -1):
            ans[i-1] = ans[i-1] + \
                right_min if right_min < nums[i] else float('inf')
            right_min = min(right_min, nums[i])

        return min(ans) if min(ans) != float('inf') else -1
