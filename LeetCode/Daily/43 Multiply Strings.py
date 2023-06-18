'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def summation(self, a, b) -> str:
            s = []
            i, j, carry = len(a)-1, len(b)-1, 0
            while i >= 0 or j >= 0 or carry:
                if i >= 0:
                    carry += int(a[i])
                    i -= 1
                if j >= 0:
                    carry += int(b[j])
                    j -= 1
                s.append(str(carry % 10))
                carry //= 10
            return ''.join(reversed(s))

        def multiply(self, num1: str, num2: str) -> str:
            if num1=="0" or num2=="0": return "0"
            ans = "0"
            for j in range(len(num2)-1, -1, -1):
                carry = 0
                mul = []
                for i in range(len(num1)-1, -1, -1):
                    carry += int(num1[i]) * int(num2[j])
                    mul.append(str(carry % 10))
                    carry //= 10
                if carry !=0: mul.append(str(carry))
                mul = ''.join(reversed(mul)) + "0"*(len(num2)-1-j)
                ans = Solution().summation(ans, mul)
            return ans

    Solution().multiply()


if __name__ == "__main__":
    main()



