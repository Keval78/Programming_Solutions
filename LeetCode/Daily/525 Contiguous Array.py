from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prev = {0: -1}
        count = 0
        maxi = 0
        for i, num in enumerate(nums):
            count += -1 if num == 0 else 1
            if count in prev:
                maxi = max(maxi, i-prev.get(count))
            else:
                prev[count] = i
        return maxi


