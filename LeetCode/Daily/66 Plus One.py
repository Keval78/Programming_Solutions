'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from collections import Counter

def main():
    class Solution:
        def plusOne(self, digits: List[int]) -> List[int]:
            for i in range(1, len(digits)+1):
                if digits[-i] == 9:
                    digits[-i] = 0
                else:
                    digits[-i] += 1
                    break        
            if i==len(digits) and digits[0]==0:
                return [1] + digits
            else:
                return digits
    
    Solution().plusOne()


if __name__ == "__main__":
    main()
