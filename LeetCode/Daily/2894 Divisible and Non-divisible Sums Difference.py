'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div = [i for i in range(m, n+1, m)]
        ndiv = [i for i in range(1, n+1) if i not in div]

        return sum(ndiv) - sum(div)
