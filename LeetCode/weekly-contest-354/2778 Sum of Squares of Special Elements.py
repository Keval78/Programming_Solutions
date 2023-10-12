from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total, n = 0, len(nums)
        for i in range(n):
            total += nums[i]*nums[i] if n % (i+1) == 0 else 0
        return total
