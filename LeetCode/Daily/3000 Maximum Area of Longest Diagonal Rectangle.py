'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = max_daig = 0
        for l, w in dimensions:
            if max_daig <= (l*l + w*w):
                max_area = max(max_area, l*w) if max_daig == (l*l + w*w) else l*w
                max_daig = l*l + w*w
        return max_area



dimensions = [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]
ans = Solution().areaOfMaxDiagonal(dimensions)
print(ans)

