'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''


class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci = [0, 1, 1]

        for i in range(3, n+1):
            tribonacci[i % 3] = sum(tribonacci)

        return tribonacci[n % 3]
