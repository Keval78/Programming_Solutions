'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from bisect import bisect


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 1, n-1
        while i<n and nums[i] > nums[i-1]: i+=1
        if i == n: return (n*(n+1))//2
        
        while j>0 and nums[j] > nums[j-1]: j-=1
        arr = nums[j:]
        
        ans = 0
        for k in range(i+1):
            if k==0: ans += n-j+1
            else: ans += n-j-bisect(arr, nums[k-1])+1
        return ans
        
        


nums = [1,2,3,4]
ans = Solution().incremovableSubarrayCount(nums)
print(ans)


nums = [6,5,7,8]
ans = Solution().incremovableSubarrayCount(nums)
print(ans)

nums = [8,7,6,6]
ans = Solution().incremovableSubarrayCount(nums)
print(ans)
