'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = []
        n = len(nums)
        for idx in range(n):
            arr.append((nums[idx], idx))    
        arr.sort()
        # print(arr)

        idx = 0
        indices, values = [], []
        while idx < n:
            if not indices or arr[idx][0]-arr[idx-1][0] <= limit:
                heappush(indices, arr[idx][1])
                heappush(values, arr[idx][0])
                idx += 1
            else:
                while indices:
                    nums[heappop(indices)] = heappop(values)

        while indices:
            nums[heappop(indices)] = heappop(values)
            
        # print(nums)
        return nums



nums = [1,5,3,9,8]
limit = 2
ans = Solution().lexicographicallySmallestArray(nums, limit)
print(ans)


nums = [1,7,6,18,2,1]
limit = 3
ans = Solution().lexicographicallySmallestArray(nums, limit)
print(ans)

nums = [1,7,28,19,10]
limit = 3
ans = Solution().lexicographicallySmallestArray(nums, limit)
print(ans)

