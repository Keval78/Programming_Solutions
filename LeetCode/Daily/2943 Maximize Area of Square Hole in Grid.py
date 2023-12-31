'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
import itertools

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        def max_consecutive_group_size(arr):
            res = 1
            for key, group in itertools.groupby(enumerate(arr), lambda x: x[0] - x[1]):
                m = len(list(group))
                res = max(res, m)
            return res
        
        max_h = max_consecutive_group_size(hBars) + 1
        max_w = max_consecutive_group_size(vBars) + 1
        ans = min(max_h, max_w)
        
        return (ans * ans) % (10**9+7) if ans != -1 else -1