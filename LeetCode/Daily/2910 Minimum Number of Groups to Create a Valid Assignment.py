'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import Counter


class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        mv = len(nums)
        for k, v in cntr.items():
            mv = min(mv, v)

        ans = 0
        def possible_partition(x, v): return True if v % x <= v//x else False
        for i in range(1, mv+1):
            total = 0
            for k, v in cntr.items():
                if possible_partition(i, v):
                    total += v//(i+1) + (1 if v %
                                         (i+1) else 0) if v > (i+1) else 1
                else:
                    total = 0
                    break
            if total:
                ans = total
        # print(ans)
        return ans
