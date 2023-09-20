"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [True]*(n+2)
        sieve[0] = sieve[1] = False
        i = 2
        while i*i <= n+2:
            if sieve[i]:
                for j in range(i*i, n+2, i):
                    sieve[j] = False
            i += 1

        primes = 0
        for i in range(2, n):
            if sieve[i]:
                primes += 1

        return primes
