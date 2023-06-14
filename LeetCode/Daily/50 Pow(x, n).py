'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def myPow(self, x: float, n: int) -> float:
            ans = 1
            power = abs(n)
            while power>0:
                if power&1:
                    ans = ans*x
                x = x*x
                power = power >> 1
            return 1/ans if n<0 else ans

    Solution().myPow()


if __name__ == "__main__":
    main()



