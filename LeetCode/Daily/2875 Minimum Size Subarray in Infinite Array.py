'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import math
from typing import List
# from collections import defaultdict
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        snums, n = sum(nums), len(nums)
        if target % snums == 0:
            return target//snums * n

        length = 0
        if target > snums:
            factor = target // snums
            target -= snums * factor
            length += n * factor
        # print(target)

        nums = nums + nums
        n = len(nums)

        i, j = 0, 0

        total = 0
        min_len = INF
        while i < n and j < n:
            if total < target:
                total += nums[j]
                j += 1
            elif total > target:
                total -= nums[i]
                i += 1
            else:
                target_len = j-i
                total += nums[j]
                j += 1
                # print(i, j, target_len)
                min_len = min(min_len, target_len)
            # print(i, j)
        # print("length", length, min_len)
        if min_len == INF:
            return -1
        return length + min_len
