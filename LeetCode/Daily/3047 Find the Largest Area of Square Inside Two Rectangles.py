'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                # Pair i, j
                # print(i, j)
                
                # Intersection possible
                # area?
                # bottomLeft[j] -> topRight[i]

                x1, x2 = max(bottomLeft[j][0], bottomLeft[i][0]), min(topRight[j][0], topRight[i][0])
                y1, y2 = max(bottomLeft[j][1], bottomLeft[i][1]), min(topRight[j][1], topRight[i][1])

                side = min(x2-x1, y2-y1)
                if side > 0:
                    max_area = max(max_area, side*side)

        return max_area