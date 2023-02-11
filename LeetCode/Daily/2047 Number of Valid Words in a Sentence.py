'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import re

def main():
    class Solution:
        def countValidWords(self, sentence: str) -> int:
            import re
            pattern = re.compile(r"^([a-z]+\-?[a-z]+[!\.,]?)$|^([a-z]*[!\.,]?)$")
            count = 0
            for word in sentence.split():
                match = re.match(pattern, word)
                if match: count+=1    
            return count
            
    Solution().countValidWords("alice and  bob are playing stone-game10")


if __name__ == "__main__":
    main()
