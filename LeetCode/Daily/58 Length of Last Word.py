'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def lengthOfLastWord(self, s: str) -> int:
            count = 0
            s = s.strip()
            for i in range(1,len(s)+1):
                if s[-i] == " ": break
                else: count+=1
            return count
    
    Solution().lengthOfLastWord()


if __name__ == "__main__":
    main()
