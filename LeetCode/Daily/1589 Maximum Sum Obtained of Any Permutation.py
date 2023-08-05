from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        ranges = [0 for i in range(n+1)]
        for req in requests:
            ranges[req[0]] += 1
            ranges[req[1]+1] -= 1
        for i in range(n):
            ranges[i+1] += ranges[i]
        ranges.sort(reverse=True)
        nums.sort(reverse=True)

        ans, MOD = 0, 10**9+7
        for i in range(n):
            ans += (nums[i]*ranges[i]) % MOD
            ans %= MOD
        return ans
