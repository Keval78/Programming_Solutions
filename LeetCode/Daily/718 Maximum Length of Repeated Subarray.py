from typing import List


class Solution:
    def findLength1(self, nums1: List[int], nums2: List[int]) -> int:
        # Dynamic Programming:
        n, m = len(nums1), len(nums2)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
        return max(max(row) for row in dp)

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Sliding Window
        m, n = len(nums1), len(nums2)
        maxCount = 0
        for i in range(-n + 1, m):
            count = 0
            for j in range(n):
                if i + j < 0:
                    continue
                elif i + j >= m:
                    break
                elif nums1[i + j] == nums2[j]:
                    count += 1
                    maxCount = max(maxCount, count)
                else:
                    count = 0
        return maxCount
