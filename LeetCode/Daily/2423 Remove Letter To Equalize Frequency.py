'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import Counter

def main():
    class Solution:
        def equalFrequency(self, word: str) -> bool:
            for i in range(len(word)):
                if len(set(Counter(word[0:i] + word[i+1:]).values())) == 1:
                    return True
                return False
    
    Solution().equalFrequency("abc")


if __name__ == "__main__":
    main()
