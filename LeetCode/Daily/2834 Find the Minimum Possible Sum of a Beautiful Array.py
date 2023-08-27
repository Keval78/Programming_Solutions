"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        ans = [(i+1) for i in range(min(n, target//2))]
        # print(ans)
        i = 0
        while len(ans) < n:
            ans.append(target+i)
            i += 1
        # print(ans)
        return sum(ans)
