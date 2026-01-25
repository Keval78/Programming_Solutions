'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(nums[i] + nums[~i] for i in range(len(nums) // 2))