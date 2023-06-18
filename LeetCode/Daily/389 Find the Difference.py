'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def findTheDifference(self, s: str, t: str) -> str:
            freq = [0]*26
            for i in t:
                freq[ord(i)-97] += 1
            for i in s:
                freq[ord(i)-97] -= 1
            for i in range(0, len(freq)):
                if freq[i]>0:
                    return chr(i+97)
            
    Solution().findTheDifference()


if __name__ == "__main__":
    main()
