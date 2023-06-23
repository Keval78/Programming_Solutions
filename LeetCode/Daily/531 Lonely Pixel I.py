"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        # Can you solve with Space Complexity: O(1)?
        def findLonelyPixel(self, picture: List[List[str]]) -> int:
            m, n = len(picture), len(picture[0])
            row_prefix, col_prefix = [0]*m, [0]*n

            for i in range(m):
                for j in range(n):
                    if picture[i][j] == "B":
                        row_prefix[i], col_prefix[j] = row_prefix[i]+1, col_prefix[j]+1
            ones = 0
            for i in range(m):
                for j in range(n):
                    if picture[i][j] == "B" and \
                        row_prefix[i] == 1 and col_prefix[j] == 1:
                        ones += 1
            return ones


    Solution().findLonelyPixel()


if __name__ == "__main__":
    main()
