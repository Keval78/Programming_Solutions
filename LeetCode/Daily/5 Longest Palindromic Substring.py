'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

# import collections
from collections import Counter, defaultdict

# import maths functions & constants
from math import gcd
from cmath import inf

# import functools.
from functools import reduce

# import Generic Type
from typing import Generic, TypeVar


class Solution:
    def longestPalindrome1(self, s: str) -> str:
        # Solution 1 (Bruteforce)
        # O(N^3)
        def is_palindrome(s: str) -> bool:
            n = len(s)
            for i in range(n//2):
                if s[i] != s[n-i-1]:
                    return False
            return True
        n = len(s)
        max_len = 0
        pal = ""
        for L in range(n):
            for R in range(L, n):
                if R+1-L > max_len and is_palindrome(s[L:R+1]):
                    max_len = R+1-L
                    pal = s[L:R+1]
        return pal

    def longestPalindrome2(self, s: str) -> str:
        # Solution 2 (DP)
        # Time: O(N^2)
        # Space: O(N^2)
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        pair = (0, 0)

        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                pair = (i, i+1)

        for diff in range(2, n):
            for i in range(n-diff):
                j = i+diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    pair = (i, j)
        return s[pair[0]: pair[1]+1]

    def longestPalindrome3(self, s: str) -> str:
        # Solution 3 (Two pointer Approcach)
        # Time: O(N^2)
        # Space: O(1)
        n = len(s)
        pal = ""
        max_len = 0
        for i in range(n):
            L, R = i, i
            while L >= 0 and R < n and s[L] == s[R]:
                L -= 1
                R += 1
            if max_len < R-L-1:
                max_len = R-L-1
                pal = s[L+1: R]

        for i in range(n-1):
            if s[i] != s[i+1]:
                continue
            L, R = i, i+1
            while L >= 0 and R < n and s[L] == s[R]:
                L -= 1
                R += 1
            if max_len < R-L-1:
                max_len = R-L-1
                pal = s[L+1: R]
        return pal

    def longestPalindrome(self, s: str) -> str:
        # Solution 3 (Manacher's Algorithm)
        # Time: O(N)
        # Space: O(N)
        # Editorial Solution (Need to Understand...)
        s_prime = '#' + '#'.join(s) + '#'
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0

        for i in range(n):
            mirror = 2 * center - i

            if i < radius:
                palindrome_radii[i] = min(
                    radius - i, palindrome_radii[mirror])

            while (i + 1 + palindrome_radii[i] < n and i - 1 - palindrome_radii[i] >= 0 and s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]):
                palindrome_radii[i] += 1

            if i + palindrome_radii[i] > radius:
                center = i
                radius = i + palindrome_radii[i]

        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index: start_index + max_length]

        return longest_palindrome
