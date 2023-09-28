"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        # n = len(maxHeights)
        # # print(maxHeights)
        # res = 0
        # for i in range(n):
        #     ans = 0
        #     j = i
        #     peak = maxHeights[i]

        #     while j >= 0:
        #         peak = min(peak, maxHeights[j])
        #         ans += peak
        #         # ans.append(peak)
        #         j -= 1

        #     j = i
        #     peak = maxHeights[j]
        #     while j < n-1:
        #         j += 1
        #         peak = min(peak, maxHeights[j])
        #         ans += peak
        #         # ans.append(peak)

        #     res = max(res, ans)

        # return res

        n = len(maxHeights)
        # print(maxHeights)

        # stack -> finding right slope for each element.

        left, right = [-1]*n, [n]*n
        stack = []
        for i, num in enumerate(maxHeights):
            while stack and maxHeights[stack[-1]] >= num:
                past = stack.pop()
                right[past] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            if left[i] == -1:
                left[i] = (left[i], maxHeights[i])
            else:
                left[i] = (left[i], maxHeights[left[i]])

            if right[i] == n:
                right[i] = (right[i], maxHeights[i])
            else:
                right[i] = (right[i], maxHeights[right[i]])

        res = 0
        for i in range(n):
            peak = maxHeights[i]
            ans = -maxHeights[i]
            j = i
            while j < n:
                nj, val = right[j]
                ans += (nj - j)*peak
                # print(str(peak) * (nj - j), end = "")
                peak = val
                j = nj
            # print()

            j = i
            peak = maxHeights[i]
            while j >= 0:
                nj, val = left[j]
                ans += (j-nj)*peak
                # print(str(peak) * (j - nj), end = "")
                peak = val
                j = nj

            # print()

            res = max(res, ans)
            # print(res)
        return res
