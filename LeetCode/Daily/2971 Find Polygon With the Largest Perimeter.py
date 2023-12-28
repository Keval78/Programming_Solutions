'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n, ans, pref = len(nums), -1, nums[0]
        
        for i in range(1, n):
            if i>1 and pref > nums[i]: ans = pref + nums[i]
            pref += nums[i]
       
        return ans


nums = [5,5,5]
ans = Solution().largestPerimeter(nums)
print(ans)


nums = [1,12,1,2,5,50,3]
ans = Solution().largestPerimeter(nums)
print(ans)

nums = [5,5,50]
ans = Solution().largestPerimeter(nums)
print(ans)
