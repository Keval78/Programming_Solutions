"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""


def main():
    class Solution:
        def isOneEditDistance(self, s: str, t: str) -> bool:
            if abs(len(s)-len(t)) > 1 or s == t:
                return False
            len_s, len_t = len(s), len(t)
            i, j = 0, 0
            count = 0
            while (i < len_s and j < len_t):
                if s[i] == t[j]:
                    i, j = i+1, j+1
                else:
                    count += 1
                    if count > 1:
                        return False
                    if len_s > len_t:
                        i += 1
                    elif len_s < len_t:
                        j += 1
                    else:
                        i, j = i+1, j+1
            return True


if __name__ == "__main__":
    main()
