'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from collections import defaultdict

def main():
    class Solution:
        def findArray(self, pref: List[int]) -> List[int]:
            return [pref[i] if i==0 else pref[i-1]^pref[i] for i in range(len(pref))]

            
    Solution().findArray(pref = [5,2,0,3,1])


if __name__ == "__main__":
    main()
