'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Sliding Window
        i, j, n = 0, 0, len(nums)
        cntr = defaultdict(int)
        ans = 0
        
        while i < n and j < n:
            while j < n:
                if cntr[nums[j]] == k: break
                cntr[nums[j]] += 1
                j+=1
            
            curr_len = j - i
            # print(i, j, nums[i:j], curr_len)
            ans = max(ans, curr_len)

            while i < n and j < n and cntr[nums[j]] == k:
                cntr[nums[i]] -= 1
                i+=1

        return ans


nums = [1,2,3,1,2,3,1,2]
k = 2
ans = Solution().maxSubarrayLength(nums, k)
print(ans)

nums = [1,2,1,2,1,2,1,2]
k = 1
ans = Solution().maxSubarrayLength(nums, k)
print(ans)

nums = [5,5,5,5,5,5,5]
k = 4
ans = Solution().maxSubarrayLength(nums, k)
print(ans)
