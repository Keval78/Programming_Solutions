"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(nums, target, start, end, res):
            i, j = start, end
            curr = nums[i] + nums[j]
            while i < j:
                # print(i, j)
                curr = nums[i] + nums[j]
                if target < curr: j -= 1
                elif target > curr: i += 1
                else: 
                    res.append([-target, nums[i], nums[j]])
                    # yield nums[i], nums[j]
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i += 1
        # -4 -1 -1 0 1 2
        res = []
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0: break
            if i==0 or nums[i] != nums[i-1]:
                twoSum(nums, -nums[i], i+1, n-1, res)
        return res
