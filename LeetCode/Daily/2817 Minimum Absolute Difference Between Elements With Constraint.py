from typing import List
import bisect


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = float('inf')

        curr = []
        for i in range(x, n):
            bisect.insort(curr, nums[i-x])
            if len(curr) == 1:
                ans = min(ans, abs(nums[i]-curr[0]))
            else:
                ind = bisect.bisect_left(curr, nums[i])
                ans = min(ans, abs(nums[i] - curr[ind-1]))
                if ind < i-x+1:
                    ans = min(ans, abs(nums[i] - curr[ind]))

        return ans
