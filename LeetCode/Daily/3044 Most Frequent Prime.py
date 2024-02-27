'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import defaultdict

class Solution:

    # def __init__(self):
    #     self.sieve = [True]*(10**6+2)
    #     self.sieve[0] = self.sieve[1] = False
    #     i = 2
    #     while i*i <= 10**6+2:
    #         if self.sieve[i]:
    #             for j in range(i*i, 10**6+2, i):
    #                 self.sieve[j] = False
    #         i += 1

    def is_prime(self, n):
        if n % 2 == 0: return False
        k = 3
        while k*k <= n:
            if n % k == 0: return False
            k += 2
        return True

    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        cntr = defaultdict(int)

        n, m  = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                # Traverse 8 Directions:

                # Traverse East side
                num = mat[i][j]
                k = j+1
                while k < m:
                    num = num*10 + mat[i][k]
                    if self.is_prime(num): cntr[num] += 1
                    k += 1
                
                # Traverse SouthEast side
                num = mat[i][j]
                l, k = i+1, j+1
                while l < n and k < m:
                    num = num*10 + mat[l][k]
                    if self.is_prime(num): cntr[num] += 1
                    l, k = l+1, k+1
                

                # Traverse South side
                num = mat[i][j]
                l = i+1
                while l < n:
                    num = num*10 + mat[l][j]
                    if self.is_prime(num): cntr[num] += 1
                    l = l+1
                
                # Traverse SouthWest side
                num = mat[i][j]
                l, k = i+1, j-1
                while l<n and k>=0:
                    num = num*10 + mat[l][k]
                    if self.is_prime(num): cntr[num] += 1
                    l, k = l+1, k-1
                
                # Traverse West side
                num = mat[i][j]
                k = j-1
                while k>=0:
                    num = num*10 + mat[i][k]
                    if self.is_prime(num): cntr[num] += 1
                    k = k-1
                
                # Traverse NorthWest side
                num = mat[i][j]
                l, k = i-1, j-1
                while l>=0 and k>=0:
                    num = num*10 + mat[l][k]
                    if self.is_prime(num): cntr[num] += 1
                    l, k = l-1, k-1
                
                # Traverse North side
                num = mat[i][j]
                l = i-1
                while l>=0:
                    num = num*10 + mat[l][j]
                    if self.is_prime(num): cntr[num] += 1
                    l = l-1

                # Traverse NorthEast side
                num = mat[i][j]
                l, k = i-1, j+1
                while l>=0 and k<m:
                    num = num*10 + mat[l][k]
                    if self.is_prime(num): cntr[num] += 1
                    l, k = l-1, k+1

        ans = -1
        if len(cntr) > 0:
            ans = max(cntr, key = lambda x: (cntr.get(x), x) )

        return ans