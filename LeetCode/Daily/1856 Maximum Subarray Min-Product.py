from typing import List
from collections import deque


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD, maxi = 10 ** 9 + 7, 0
        arr = nums
        nn = len(arr)

        pref = [0] + list(arr)
        for i in range(1, nn+1):
            pref[i] += pref[i-1]

        left = [-1] * nn
        right = [nn] * nn
        stack = deque()
        for i in range(nn):
            while stack and arr[stack[-1]] > arr[i]:
                past = stack.pop()
                right[past] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        # print(left, right)

        for i in range(nn):
            rng_min = arr[i]
            rng_sum = pref[right[i]] - pref[left[i]+1]
            # print(rng_min * rng_sum)
            maxi = max(maxi, (rng_min*rng_sum))

        return maxi % MOD
