from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total != ((n-1)*n)//2 + (n-1):
            return False
        nums.sort()
        for i, num in enumerate(nums):
            if (i+1) != n and num != (i+1):
                return False
        return True
