'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        # TODO: Solution Approach
        # TODO: Last Index match + Sliding Window
        
        # * Find the last index of each number. 
        # * First & Last index should be always in the same partition.
        # * Sliding Window to find the partitions.
        
        last_index = {}
        for idx, num in enumerate(nums):
            last_index[num] = idx

        n = len(nums)
        left = right = 0
        cgg = 1
        
        while left < n:
            if right < left: cgg += 1
            right = max(right, last_index[nums[left]])
            left += 1
        
        return pow(2, cgg-1, 10**9+7)


nums = [1,2,3,4]
ans = Solution().numberOfGoodPartitions(nums)
print(ans)


nums = [1,1,1,1]
ans = Solution().numberOfGoodPartitions(nums)
print(ans)

nums = [1,2,1,3]
ans = Solution().numberOfGoodPartitions(nums)
print(ans)

