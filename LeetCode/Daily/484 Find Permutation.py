"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def findPermutation(self, s: str) -> List[int]:
            n = len(s)
            output = [i+1 for i in range(n+1)]
            i = 1
            while i <= n:
                j = i
                while i<=n and s[i-1]=="D": i+=1
                output[j-1:i] = reversed(output[j-1:i])
                i+=1
            return output

    Solution().findPermutation()


if __name__ == "__main__":
    main()
