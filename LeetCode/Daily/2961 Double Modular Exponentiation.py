'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            if target == pow(pow(a, b, 10), c, m):
                ans.append(i)
        return ans


variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]]
target = 2
ans = Solution().getGoodIndices(variables, target)
print(ans)

variables = [[39,3,1000,1000]]
target = 17
ans = Solution().getGoodIndices(variables, target)
print(ans)

