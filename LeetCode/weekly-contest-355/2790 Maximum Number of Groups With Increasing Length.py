from typing import List


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        curr, groups = 0, 0
        for i, num in enumerate(usageLimits):
            curr += num
            if curr >= ((groups+1)*(groups+2))//2:
                groups += 1
        return groups
