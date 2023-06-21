"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def stringShift(self, s: str, shift: List[List[int]]) -> str:
            n = len(s)
            total_shift = 0
            for shi in shift:
                total_shift += 0-shi[1] if shi[0] == 0 else shi[1]
            #print(total_shift)
            total_shift = total_shift%n
            #print(total_shift)
            return s[n-total_shift:] + s[:n-total_shift]
            
    Solution().stringShift()


if __name__ == "__main__":
    main()
