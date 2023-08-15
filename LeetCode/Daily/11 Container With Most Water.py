from typing import List
from collections import deque
import bisect


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        stack = deque()

        left, right = [0], [0]
        lind, rind = [-1], [-1]
        uniqs = set()
        for i in range(n):
            if height[i] > left[-1]:
                left.append(height[i])
                lind.append(i)
                uniqs.add(height[i])
            if height[n-i-1] > right[-1]:
                right.append(height[n-i-1])
                rind.append(n-i-1)
                uniqs.add(height[n-i-1])

        # print(left, right)
        # print(lind, rind)
        # print(uniqs)
        maxi = 0
        for val in uniqs:
            lval = bisect.bisect_left(left, val)
            rval = bisect.bisect_left(right, val)
            # print(val, lind[lval], rind[rval])
            maxi = max(maxi, (rind[rval]-lind[lval])*val)
        return maxi
