"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        # print(maxHeights)

        left, right = [(-1, maxHeights[i])
                       for i in range(n)], [(n, maxHeights[i]) for i in range(n)]
        stack = []
        for i, num in enumerate(maxHeights):
            while stack and maxHeights[stack[-1]] >= num:
                past = stack.pop()
                right[past] = (i, maxHeights[i])
            if stack:
                left[i] = (stack[-1], maxHeights[stack[-1]])
            stack.append(i)

        left_slope = [0] * n
        right_slope = [0] * n
        # For each peak count left slope
        # stack -> finding right slope for each element.
        for i in range(n):
            peak = maxHeights[i]
            j, val = left[i]

            left_slope[i] = (i - j) * peak

            if j != -1:  # Use previous counted slope
                left_slope[i] += left_slope[j]

        # print(left_slope)

        for i in range(n-1, -1, -1):
            peak = maxHeights[i]
            j, val = right[i]

            right_slope[i] = (j-i) * peak

            if j != n:  # Use previous counted slope
                right_slope[i] += right_slope[j]

        # print(right_slope)

        res = max([i+j-k for i, j, k in zip(left_slope, right_slope, maxHeights)])
        print(res)
        return res
