"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        if sum(nums) == target:
            return 0
        counts = [0 for i in range(32)]
        for num in nums:
            bit = int(math.log(num, 2))
            counts[bit] += 1
        # print(counts[:10])

        need = []
        num = target
        for i in range(32):
            if num & 1 == 1:
                need.append(1)
            else:
                need.append(0)
            num = num >> 1
            # need[i] = counts[i] - need[i]

        # print(need[:10])
        op = 0
        forward = 0
        for i in range(32):
            counts[i] += forward
            if need[i] > 0:
                if counts[i] > 0:
                    counts[i] -= 1
                else:
                    # bring from the next set bit
                    j = i+1
                    while j < 32 and counts[j] == 0:
                        j += 1
                    counts[j] -= 1
                    op += (j-i)
                    while j > i:
                        j -= 1
                        counts[j] += 1
            forward = counts[i]//2
            counts[i] %= 2
        # print(counts)

        return op
