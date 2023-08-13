from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        digits = [[] for i in range(10)]

        for i, num in enumerate(nums):
            mdigit = 0
            while num > 0:
                mdigit = max(mdigit, num % 10)
                num //= 10

            digits[mdigit].append(nums[i])

        ans = -1
        for vals in digits:
            if len(vals) >= 2:
                vals.sort()
                ans = max(ans, vals[-1]+vals[-2])

        return ans
