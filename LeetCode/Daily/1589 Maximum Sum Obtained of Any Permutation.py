from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        ranges = [[0, i] for i in range(n+1)]
        for req in requests:
            ranges[req[0]][0] += 1
            ranges[req[1]+1][0] -= 1
        for i in range(n):
            ranges[i+1][0] += ranges[i][0]
        ranges.sort(key=lambda x: -x[0])
        nums.sort(reverse=True)

        ans, MOD = 0, 10**9+7
        for i in range(n):
            ans += (nums[i]*ranges[i][0]) % MOD
            ans %= MOD
        return ans
