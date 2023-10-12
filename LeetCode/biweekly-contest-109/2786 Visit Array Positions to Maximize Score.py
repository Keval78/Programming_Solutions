from typing import List


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        max_score = [0, 0]
        ans = 0
        n = len(nums)
        for i in range(n-1, -1, -1):
            parity = nums[i] % 2
            ans = max(0, max_score[parity], max_score[1-parity]-x) + nums[i]
            max_score[parity] = max(ans, max_score[parity])
        return ans
