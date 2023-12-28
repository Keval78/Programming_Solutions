'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        for i in range(0, n, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

nums = [5,4,2,3]
ans = Solution().numberGame(nums)
print(ans)


nums = [2,5]
ans = Solution().numberGame(nums)
print(ans)
