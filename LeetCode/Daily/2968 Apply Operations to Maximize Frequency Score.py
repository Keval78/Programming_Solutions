'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        pref = [0] + nums
        for i in range(n): pref[i+1] += pref[i]

        def isSubarrayPossible(m):
            for i in range(n-m+1):
                # print("sub", nums[i:m+i], end= " ")
                midx = m//2
                # print(i, midx, pref[midx+i+1] - pref[i], pref[m+i] - pref[midx+i+1])
                lcost = (pref[midx+i+1] - pref[i]) - nums[midx+i]*(midx+1)
                rcost = (pref[m+i] - pref[midx+i+1]) - nums[midx+i]*(m-midx-1)

                # print(abs(lcost), abs(rcost))
                if abs(lcost) + abs(rcost) <= k:
                    return True
            
            return False
        
        # Binary Search
        l, r = 1, n
        ans = 1
        while l <= r:
            mid = (l+r)//2
            if isSubarrayPossible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans



nums = [1,2,6,4]
k = 3
ans = Solution().maxFrequencyScore(nums, k)
print(ans)


nums = [1,4,4,2,4]
k = 0
ans = Solution().maxFrequencyScore(nums, k)
print(ans)

nums = [1,4,4,2,4]
k = 5
ans = Solution().maxFrequencyScore(nums, k)
print(ans)