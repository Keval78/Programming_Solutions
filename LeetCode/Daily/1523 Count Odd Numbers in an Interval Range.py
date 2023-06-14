'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def countOdds(self, low: int, high: int) -> int:
            return ((high-low)//2)+1 if (high|low)&1==1 else (high-low)//2
            
    Solution().countOdds()


if __name__ == "__main__":
    main()



