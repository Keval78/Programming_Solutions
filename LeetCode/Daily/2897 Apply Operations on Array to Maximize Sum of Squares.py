'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = [0]*n
        for i in range(32):
            j, bit = 0, 1 << i
            for num in nums:
                if num & bit:
                    arr[j] += bit
                    j += 1

        ans, MOD = 0, 10**9+7
        for i in range(k):
            ans += arr[i]*arr[i]
            ans %= MOD

        return ans
