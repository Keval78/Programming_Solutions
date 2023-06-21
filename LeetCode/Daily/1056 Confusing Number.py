"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def confusingNumber(self, n: int) -> bool:
            reverse = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
            corr_n, rev_n = n, 0
            while(n>0):
                digit = n % 10
                n //= 10
                if reverse[digit] == -1: return False
                rev_n = rev_n*10 + reverse[digit]
            return True if corr_n != rev_n else False
            
    Solution().confusingNumber()


if __name__ == "__main__":
    main()
