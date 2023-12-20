'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k: return []
            ans.append([nums[i], nums[i+1], nums[i+2]])
        return ans


nums = [1,3,4,8,7,9,3,5,1]
k = 2
ans = Solution().divideArray(nums, k)
print(ans)


nums = [1,3,3,2,7,3]
k = 3
ans = Solution().divideArray(nums, k)
print(ans)
