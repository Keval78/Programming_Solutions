"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        pairs = {}
        for u, v in coordinates:
            pairs[(u, v)] = pairs.get((u, v), 0) + 1

        ans = 0
        for i in range(k+1):
            # i, k-i
            for x1, y1 in coordinates:
                x2, y2 = x1 ^ i, y1 ^ (k-i)
                if x1 == x2 and y1 == y2:
                    ans += pairs[(x2, y2)] - 1
                else:
                    ans += pairs.get((x2, y2), 0)
        return ans//2
