'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        if sum(nums) + n > m: return -1
        
        last = set(changeIndices)
        for i in range(n):
            if (i+1) not in last:
                return -1


        def isPossible(m):
            last = [[-1, i] for i in range(n)]
            for i in range(m):
                last[changeIndices[i]-1] = [i, changeIndices[i]-1]
            last.sort()
            if last[0][0] == -1: return False

            used = 0
            for op, idx in last:
                if nums[idx] <= op - used: used += nums[idx] + 1
                else: return False
            return True
        
        l, r = 0, m+1
        ans = -1
        while l < r:
            mid = (l+r)//2
            if isPossible(mid):
                ans = mid
                r = mid
            else:
                l = mid+1
        return ans