'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        left = right = 0
        n, maxi = len(nums), max(nums)
        k_count = 0

        while left < n and right < n:
            while right < n:
                if nums[right] == maxi:
                    k_count += 1
                right += 1
                if k_count == k: break

            
            while left < n:
                if k_count == k: cnt += n-right+1
                if nums[left] == maxi:
                    k_count -= 1
                left += 1
                if k_count < k: break
        
        return cnt


nums = [1,3,2,3,3]
k = 2
ans = Solution().countSubarrays(nums, k)
print(ans)

nums = [1,4,2,1]
k = 3
ans = Solution().countSubarrays(nums, k)
print(ans)

