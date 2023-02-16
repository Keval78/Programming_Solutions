'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def mySqrt(self, x: int) -> int:
            sqrt, i = 0, 1
            while x>=i:
                x -= i
                sqrt, i = sqrt+1, i+2
            return sqrt
            
    Solution().mySqrt(x=4)


if __name__ == "__main__":
    main()
