"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        n, m = len(slots1), len(slots2)
        L, R = 0, 0

        while L < n and R < m:
            if slots2[R][0] > slots1[L][1]:
                L += 1
            elif slots1[L][0] > slots2[R][1]:
                R += 1
            else:
                d = min(slots1[L][1], slots2[R][1]) - \
                    max(slots1[L][0], slots2[R][0])
                # print(d, L, R)
                if d >= duration:
                    start = max(slots1[L][0], slots2[R][0])
                    return [start, start+duration]
                if (slots1[L][1] < slots2[R][1]):
                    L += 1
                else:
                    R += 1
        return []
