'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import Counter


def main():
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            freq = [0]*26
            for i in range(min(len(s), len(t))):
                freq[ord(s[i])-97] += 1
                freq[ord(t[i])-97] -= 1
            return all([v == 0 for v in freq])


if __name__ == "__main__":
    main()
