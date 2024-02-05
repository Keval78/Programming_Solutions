'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def requireOperation(self, nums: List[int], bits: int):
        # Require operations to set all bits to zero in nums:
        op, prev, val = 0, 0, bits
        for ind, num in enumerate(nums):
            if num & bits == 0: continue

            if ind-1 != prev:
                val = bits

            val &= nums[ind]
            op += 1            
            if val == 0: 
                val = bits
                op -= 1

            prev = ind
        return op



    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        bits = minor = 0
        for bit in range(30, -1, -1):            
            # print(bit, bits | (1 << bit))
            op = self.requireOperation(nums, bits | (1 << bit))
            if op <= k: bits |= (1 << bit)
            else: minor |= (1 << bit)
            
        return minor


nums = [3,5,3,2,7]
k = 2
ans = Solution().minOrAfterOperations(nums, k)
print(ans)

nums = [7,3,15,14,2,8]
k = 4
ans = Solution().minOrAfterOperations(nums, k)
print(ans)

nums = [10,7,10,3,9,14,9,4]
k = 1
ans = Solution().minOrAfterOperations(nums, k)
print(ans)

nums = [9,6,12,6,13,14,12,8,0,10]
k = 6
ans = Solution().minOrAfterOperations(nums, k)
print(ans)

nums = [1073709056,32768]
k = 1
ans = Solution().minOrAfterOperations(nums, k)
print(ans)

