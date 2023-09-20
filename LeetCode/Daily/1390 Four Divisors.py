"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        def divisors(n: int):
            div, i = 0, 2
            total = 0
            while i*i <= n:
                if n % i == 0:
                    if n//i == i:
                        div += 1
                    else:
                        div += 2
                    total += i + n//i
                i += 1
            return div, total

        ans = 0
        for idx, num in enumerate(nums):
            divs, total = divisors(num)
            if divs == 2:
                ans += 1 + total + num

        return ans
