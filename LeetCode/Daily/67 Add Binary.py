'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def addBinary(self, a: str, b: str) -> str:
            s = []
            i, j, carry = len(a)-1, len(b)-1, 0
            while i >= 0 or j >= 0 or carry:
                if i >= 0:
                    carry += int(a[i])
                    i -= 1
                if j >= 0:
                    carry += int(b[j])
                    j -= 1
                s.append(str(carry % 2))
                carry //= 2
            return ''.join(reversed(s))
            
    Solution().addBinary()


if __name__ == "__main__":
    main()



