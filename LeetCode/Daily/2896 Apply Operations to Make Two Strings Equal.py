'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        if len(s1) != len(s2):
            return -1

        cnt, n = 0, len(s1)
        mismatch = []
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            cnt += 1
            mismatch.append(i)
        if cnt % 2:
            return -1

        def min_cost(i, j, memo):
            # print(i, j)
            if i >= j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            res = min(
                min(abs(mismatch[i]-mismatch[i+1]), x) +
                min_cost(i+2, j, memo),
                min(abs(mismatch[j-1]-mismatch[j]), x) +
                min_cost(i, j-2, memo),
                min(abs(mismatch[i]-mismatch[j]), x) + min_cost(i+1, j-1, memo)
            )
            memo[i][j] = res
            return res

        memo = [[-1]*len(mismatch) for i in range(len(mismatch))]
        ans = min_cost(0, len(mismatch)-1, memo)
        # print(ans)
        return ans

    def minOperations2(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        diff = []
        for i in range(n):
            if s1[i] != s2[i]:
                diff.append(i)

        print(diff)
        m = len(diff)
        if m % 2:
            return -1

        # DP with memoization
        def topdowndp(idx, op, memo):
            if idx == m:
                return 0

            if memo[idx][op] != -1:
                return memo[idx][op]

            res = x + topdowndp(idx+1, op+1, memo)
            if idx < m-1:
                res = min(res, diff[idx+1]-diff[idx] +
                          topdowndp(idx+2, op, memo))
            if op > 0:
                res = min(res, topdowndp(idx+1, op-1, memo))

            memo[idx][op] = res
            return res

        memo = [[-1]*n for i in range(n)]
        ans = topdowndp(0, 0, memo)
        return ans
